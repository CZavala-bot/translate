#!/usr/bin/env python3
"""
Ingest Docling - Lossless Document Ingestion

Converts documents (.docx, .pdf, .pptx, etc.) into structured JSON and Markdown,
preserving all information including:
- Text hierarchy (headings, paragraphs, lists)
- Tables (as structured data)
- Images/figures (extracted to assets folder)
- Code blocks, equations, hyperlinks, footnotes, headers/footers

Usage:
    Single file:
        python ingest_docling.py --input doc.pdf --output_json out.json --output_md out.md

    Batch mode:
        python ingest_docling.py --sources-dir sources/raw --output-dir ingested

Requirements:
    pip install docling pillow
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import logging
import re
import sys
import tempfile
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

# =============================================================================
# CONFIGURATION
# =============================================================================

DEFAULT_EXTS = {".pdf", ".docx", ".pptx", ".xlsx", ".html", ".htm", ".md", ".txt"}
VALID_FORMATS = {"md", "json"}
ASSETS_FOLDER = "assets"

# Configure logging with detailed format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


# =============================================================================
# DATA STRUCTURES
# =============================================================================
# These dataclasses define the structured output format for the JSON file.
# They are designed to preserve all document information in a way that is
# easy for LLMs to parse and understand.

@dataclass
class DocumentMetadata:
    """Metadata about the source document."""
    source_path: str
    source_filename: str
    file_type: str
    file_size_bytes: int
    ingestion_timestamp: str
    docling_version: str = ""
    title: str = ""
    author: str = ""
    creation_date: str = ""
    modification_date: str = ""
    page_count: int = 0
    word_count: int = 0
    language: str = ""
    custom_properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TextBlock:
    """A block of text with hierarchy information."""
    type: str  # heading, paragraph, list_item, code, quote, etc.
    content: str
    level: int = 0  # For headings: 1-6, for lists: nesting level
    style: str = ""  # Additional styling info (bold, italic, etc.)
    page_number: Optional[int] = None
    bounding_box: Optional[Dict[str, float]] = None  # {x, y, width, height}


@dataclass
class TableCell:
    """A single cell in a table."""
    content: str
    row_span: int = 1
    col_span: int = 1
    is_header: bool = False


@dataclass
class Table:
    """A table extracted from the document."""
    id: str
    caption: str = ""
    headers: List[str] = field(default_factory=list)
    rows: List[List[str]] = field(default_factory=list)  # Simple representation
    cells: List[List[TableCell]] = field(default_factory=list)  # Rich representation
    page_number: Optional[int] = None
    bounding_box: Optional[Dict[str, float]] = None


@dataclass
class Figure:
    """An image or graphic extracted from the document."""
    id: str
    asset_path: str  # Relative path to the extracted image file
    alt_text: str = ""
    caption: str = ""
    figure_type: str = "image"  # image, chart, diagram, photo, etc.
    page_number: Optional[int] = None
    bounding_box: Optional[Dict[str, float]] = None
    width: Optional[int] = None
    height: Optional[int] = None
    format: str = ""  # png, jpg, etc.
    extraction_error: str = ""  # If extraction failed, explain why


@dataclass
class Hyperlink:
    """A hyperlink found in the document."""
    text: str
    url: str
    page_number: Optional[int] = None


@dataclass
class CodeBlock:
    """A code block or snippet."""
    content: str
    language: str = ""
    page_number: Optional[int] = None


@dataclass
class Equation:
    """A mathematical equation."""
    content: str  # LaTeX or MathML representation
    format: str = "latex"  # latex, mathml, image
    image_path: str = ""  # If rendered as image
    page_number: Optional[int] = None


@dataclass
class Section:
    """A section of the document with nested content."""
    id: str
    title: str
    level: int
    content: List[TextBlock] = field(default_factory=list)
    subsections: List["Section"] = field(default_factory=list)
    page_start: Optional[int] = None
    page_end: Optional[int] = None


@dataclass
class StructuredDocument:
    """The complete structured representation of a document."""
    metadata: DocumentMetadata
    main_text: List[Section]
    tables: List[Table]
    figures: List[Figure]
    code_blocks: List[CodeBlock]
    equations: List[Equation]
    hyperlinks: List[Hyperlink]
    footnotes: List[TextBlock]
    headers: List[TextBlock]  # Page headers
    footers: List[TextBlock]  # Page footers
    raw_text: str = ""  # Full text for search/fallback


# =============================================================================
# ARGUMENT PARSING
# =============================================================================

def parse_args() -> argparse.Namespace:
    """Parse command line arguments supporting both single file and batch modes."""
    parser = argparse.ArgumentParser(
        description="Convert documents to structured JSON and Markdown using Docling.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Single file mode:
    python ingest_docling.py --input doc.pdf --output_json out.json --output_md out.md

  Batch mode (process entire directory):
    python ingest_docling.py --sources-dir sources/raw --output-dir ingested

  With custom extensions:
    python ingest_docling.py --sources-dir sources/raw --output-dir ingested --ext pdf,docx
        """
    )

    # Single file mode arguments
    parser.add_argument(
        "--input", "-i",
        help="Path to a single input document (single file mode)"
    )
    parser.add_argument(
        "--output_json", "-oj",
        help="Path for JSON output (single file mode)"
    )
    parser.add_argument(
        "--output_md", "-om",
        help="Path for Markdown output (single file mode)"
    )

    # Batch mode arguments
    parser.add_argument(
        "--sources-dir",
        default="sources/raw",
        help="Directory with original documents (batch mode). Default: sources/raw"
    )
    parser.add_argument(
        "--output-dir",
        default="ingested",
        help="Directory for ingested outputs (batch mode). Default: ingested"
    )
    parser.add_argument(
        "--formats",
        default="md,json",
        help="Comma-separated output formats: md,json. Default: md,json"
    )
    parser.add_argument(
        "--ext",
        default=",".join(sorted(DEFAULT_EXTS)),
        help="Comma-separated file extensions to process. Default: %(default)s"
    )

    # Processing options
    parser.add_argument(
        "--recursive",
        dest="recursive",
        action="store_true",
        default=True,
        help="Scan subdirectories in batch mode. Default: true"
    )
    parser.add_argument(
        "--no-recursive",
        dest="recursive",
        action="store_false",
        help="Do not scan subdirectories."
    )
    parser.add_argument(
        "--extract-images",
        dest="extract_images",
        action="store_true",
        default=True,
        help="Extract images to assets folder. Default: true"
    )
    parser.add_argument(
        "--no-extract-images",
        dest="extract_images",
        action="store_false",
        help="Do not extract images."
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    return parser.parse_args()


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def normalize_exts(value: str) -> Set[str]:
    """Normalize file extensions to a set with leading dots."""
    exts = set()
    for part in value.split(","):
        part = part.strip().lower()
        if not part:
            continue
        if not part.startswith("."):
            part = "." + part
        exts.add(part)
    return exts


def iter_sources(sources_dir: Path, exts: Set[str], recursive: bool) -> Iterable[Path]:
    """Iterate over source files matching the given extensions."""
    if recursive:
        candidates = sources_dir.rglob("*")
    else:
        candidates = sources_dir.glob("*")
    for path in candidates:
        if path.is_file() and path.suffix.lower() in exts:
            yield path


def generate_id(prefix: str, index: int, content: str = "") -> str:
    """Generate a unique ID for document elements."""
    if content:
        hash_suffix = hashlib.md5(content.encode()).hexdigest()[:8]
        return f"{prefix}_{index}_{hash_suffix}"
    return f"{prefix}_{index}"


def sanitize_filename(name: str) -> str:
    """Sanitize a string for use as a filename."""
    # Remove or replace invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', name)
    sanitized = re.sub(r'\s+', '_', sanitized)
    return sanitized[:100]  # Limit length


# =============================================================================
# DOCUMENT EXTRACTION (using Docling)
# =============================================================================

def extract_document(source_path: Path, extract_images: bool = True) -> Tuple[Any, Optional[Any]]:
    """
    Extract document content using Docling.

    Returns:
        Tuple of (docling_document, converter_result)
    """
    try:
        from docling.document_converter import DocumentConverter
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions
        from docling.document_converter import PdfFormatOption
    except ImportError as e:
        logger.error(f"Docling not installed. Install with: pip install docling")
        raise ImportError(f"Docling required but not found: {e}")

    logger.info(f"Processing document: {source_path}")

    # Configure pipeline for comprehensive extraction
    try:
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = True  # Enable OCR for scanned documents
        pipeline_options.do_table_structure = True  # Extract table structure
        pipeline_options.generate_picture_images = extract_images
    except Exception:
        # Fallback for different Docling versions
        pipeline_options = None

    try:
        if pipeline_options:
            converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
        else:
            converter = DocumentConverter()
    except Exception:
        # Ultimate fallback
        converter = DocumentConverter()

    # Convert the document
    result = converter.convert(str(source_path))
    doc = getattr(result, "document", result)

    return doc, result


def extract_images_from_document(
    doc: Any,
    result: Any,
    output_dir: Path,
    base_name: str
) -> List[Figure]:
    """
    Extract images from the document and save them to the assets folder.

    Returns:
        List of Figure objects with paths to extracted images
    """
    figures = []
    assets_dir = output_dir / ASSETS_FOLDER / base_name
    assets_dir.mkdir(parents=True, exist_ok=True)

    # Try to access pictures from docling document
    try:
        pictures = getattr(doc, "pictures", []) or []
        if not pictures and hasattr(doc, "pages"):
            for page in doc.pages:
                page_pictures = getattr(page, "pictures", []) or []
                pictures.extend(page_pictures)
    except Exception as e:
        logger.warning(f"Could not access pictures: {e}")
        pictures = []

    for idx, picture in enumerate(pictures):
        figure_id = generate_id("fig", idx)
        image_filename = f"{figure_id}.png"
        image_path = assets_dir / image_filename
        relative_path = f"{ASSETS_FOLDER}/{base_name}/{image_filename}"

        fig = Figure(
            id=figure_id,
            asset_path=relative_path,
            figure_type="image",
            page_number=getattr(picture, "page_no", None),
        )

        # Try to extract bounding box
        try:
            if hasattr(picture, "bounding_box"):
                bbox = picture.bounding_box
                fig.bounding_box = {
                    "x": getattr(bbox, "x", 0),
                    "y": getattr(bbox, "y", 0),
                    "width": getattr(bbox, "width", 0),
                    "height": getattr(bbox, "height", 0),
                }
        except Exception:
            pass

        # Try to extract caption/alt text
        try:
            fig.caption = getattr(picture, "caption", "") or ""
            fig.alt_text = getattr(picture, "alt_text", fig.caption) or fig.caption
        except Exception:
            pass

        # Try to save the image
        try:
            saved = False

            if hasattr(picture, "image"):
                image_data = picture.image

                # Newer docling returns an ImageRef with a .pil_image attribute
                if not saved and hasattr(image_data, "pil_image"):
                    try:
                        pil_img = image_data.pil_image
                        if pil_img is not None:
                            pil_img.save(str(image_path))
                            fig.format = "png"
                            fig.width = getattr(pil_img, "width", None)
                            fig.height = getattr(pil_img, "height", None)
                            saved = True
                    except Exception as e:
                        # Fall through to other strategies
                        logger.debug(f"pil_image save failed for {figure_id}: {e}")

                if not saved and hasattr(image_data, "save"):
                    # PIL Image
                    image_data.save(str(image_path))
                    fig.format = "png"
                    fig.width = getattr(image_data, "width", None)
                    fig.height = getattr(image_data, "height", None)
                    saved = True
                elif not saved and isinstance(image_data, bytes):
                    image_path.write_bytes(image_data)
                    fig.format = "png"
                    saved = True
                elif not saved and isinstance(image_data, str):
                    # Base64 encoded
                    decoded = base64.b64decode(image_data)
                    image_path.write_bytes(decoded)
                    fig.format = "png"
                    saved = True

            elif hasattr(picture, "data"):
                image_path.write_bytes(picture.data)
                fig.format = "png"
                saved = True

            if saved:
                logger.info(f"Extracted image: {relative_path}")
            else:
                fig.extraction_error = "No image data available"
                logger.warning(f"Could not extract image {figure_id}: no data")
        except Exception as e:
            fig.extraction_error = str(e)
            logger.warning(f"Failed to extract image {figure_id}: {e}")

        figures.append(fig)

    return figures


def extract_tables_from_document(doc: Any) -> List[Table]:
    """
    Extract tables from the document.

    Returns:
        List of Table objects
    """
    tables = []

    try:
        doc_tables = getattr(doc, "tables", []) or []
    except Exception:
        doc_tables = []

    for idx, table in enumerate(doc_tables):
        table_id = generate_id("tbl", idx)

        # Extract table data
        headers = []
        rows = []
        cells = []

        try:
            # Try to get structured table data
            if hasattr(table, "data") and table.data:
                data = table.data
                grid = getattr(data, "grid", None)
                if grid:
                    # data.grid is expected to be a list of list of cells/strings
                    headers = [str(cell.text if hasattr(cell, "text") else cell) for cell in grid[0]] if grid else []
                    rows = [
                        [str(cell.text if hasattr(cell, "text") else cell) for cell in row]
                        for row in grid[1:]
                    ]
                elif isinstance(data, list) and len(data) > 0:
                    # Assume first row is header
                    if isinstance(data[0], list):
                        headers = [str(cell) for cell in data[0]]
                        rows = [[str(cell) for cell in row] for row in data[1:]]
            elif hasattr(table, "export_to_dataframe"):
                df = table.export_to_dataframe()
                headers = list(df.columns)
                rows = df.values.tolist()
            elif hasattr(table, "to_markdown"):
                # Parse markdown table
                md_table = table.to_markdown()
                lines = md_table.strip().split("\n")
                if len(lines) >= 2:
                    headers = [c.strip() for c in lines[0].split("|") if c.strip()]
                    for line in lines[2:]:  # Skip separator
                        row = [c.strip() for c in line.split("|") if c.strip()]
                        if row:
                            rows.append(row)
        except Exception as e:
            logger.warning(f"Could not extract table {table_id} structure: {e}")

        tbl = Table(
            id=table_id,
            caption=getattr(table, "caption", "") or "",
            headers=headers,
            rows=rows,
            page_number=getattr(table, "page_no", None),
        )

        # Try to get bounding box
        try:
            if hasattr(table, "bounding_box"):
                bbox = table.bounding_box
                tbl.bounding_box = {
                    "x": getattr(bbox, "x", 0),
                    "y": getattr(bbox, "y", 0),
                    "width": getattr(bbox, "width", 0),
                    "height": getattr(bbox, "height", 0),
                }
        except Exception:
            pass

        tables.append(tbl)

    return tables


def build_sections_from_document(doc: Any) -> Tuple[List[Section], List[TextBlock]]:
    """
    Build hierarchical sections from document content.

    Returns:
        Tuple of (sections list, flat text blocks list)
    """
    sections = []
    all_blocks = []
    current_section = None
    section_stack: List[Section] = []

    try:
        # Try different ways to access document content
        content_items = []

        if hasattr(doc, "main_text"):
            content_items = doc.main_text or []
        elif hasattr(doc, "body"):
            content_items = doc.body or []
        elif hasattr(doc, "iterate_items"):
            # In Docling >=2.x iterate_items returns (item, level)
            try:
                content_items = list(doc.iterate_items())
            except Exception:
                content_items = []
        elif hasattr(doc, "texts"):
            content_items = doc.texts or []

        for idx, item in enumerate(content_items):
            # Unpack tuple form (item, level) used by doc.iterate_items()
            level_override = None
            if isinstance(item, tuple) and len(item) == 2:
                item, level_override = item

            item_type = getattr(item, "label", getattr(item, "type", "paragraph"))
            if isinstance(item_type, str):
                item_type = item_type.lower()
            else:
                item_type = str(item_type).lower()

            content = ""
            if hasattr(item, "text"):
                content = str(getattr(item, "text"))
            elif hasattr(item, "content"):
                content = str(getattr(item, "content"))
            elif hasattr(item, "value"):
                content = str(getattr(item, "value"))
            elif isinstance(item, str):
                content = item

            level = level_override if level_override is not None else (getattr(item, "level", 0) or 0)

            # Create TextBlock
            block = TextBlock(
                type=item_type,
                content=content,
                level=level,
                page_number=getattr(item, "page_no", None),
            )
            all_blocks.append(block)

            # Check if this is a heading
            if "heading" in item_type or "title" in item_type:
                # Create new section
                section = Section(
                    id=generate_id("sec", idx),
                    title=content,
                    level=level if level > 0 else 1,
                    page_start=getattr(item, "page_no", None),
                )

                # Handle section hierarchy
                while section_stack and section_stack[-1].level >= section.level:
                    section_stack.pop()

                if section_stack:
                    section_stack[-1].subsections.append(section)
                else:
                    sections.append(section)

                section_stack.append(section)
                current_section = section
            else:
                # Add content to current section
                if current_section:
                    current_section.content.append(block)

    except Exception as e:
        logger.warning(f"Error building sections: {e}")

    # If no sections were created, create a default one
    if not sections and all_blocks:
        default_section = Section(
            id="sec_0_default",
            title="Document Content",
            level=1,
            content=all_blocks,
        )
        sections.append(default_section)

    return sections, all_blocks


def extract_metadata(source_path: Path, doc: Any) -> DocumentMetadata:
    """Extract metadata from the document."""
    try:
        from docling import __version__ as docling_version
    except ImportError:
        docling_version = "unknown"

    metadata = DocumentMetadata(
        source_path=str(source_path),
        source_filename=source_path.name,
        file_type=source_path.suffix.lower(),
        file_size_bytes=source_path.stat().st_size,
        ingestion_timestamp=datetime.now().isoformat(),
        docling_version=docling_version,
    )

    # Try to extract additional metadata from document
    try:
        if hasattr(doc, "metadata"):
            doc_meta = doc.metadata
            metadata.title = getattr(doc_meta, "title", "") or ""
            metadata.author = getattr(doc_meta, "author", "") or ""
            metadata.creation_date = str(getattr(doc_meta, "created", "")) or ""
            metadata.modification_date = str(getattr(doc_meta, "modified", "")) or ""
            metadata.language = getattr(doc_meta, "language", "") or ""

        if hasattr(doc, "pages"):
            metadata.page_count = len(doc.pages)

        # Count words in raw text
        if hasattr(doc, "export_to_text"):
            raw_text = doc.export_to_text()
            if raw_text:
                metadata.word_count = len(raw_text.split())
    except Exception as e:
        logger.warning(f"Could not extract some metadata: {e}")

    return metadata


def extract_hyperlinks(doc: Any) -> List[Hyperlink]:
    """Extract hyperlinks from the document."""
    hyperlinks = []

    try:
        links = getattr(doc, "links", []) or getattr(doc, "hyperlinks", []) or []
        for link in links:
            hl = Hyperlink(
                text=getattr(link, "text", "") or "",
                url=getattr(link, "url", getattr(link, "href", "")) or "",
                page_number=getattr(link, "page_no", None),
            )
            if hl.url:
                hyperlinks.append(hl)
    except Exception as e:
        logger.warning(f"Could not extract hyperlinks: {e}")

    return hyperlinks


def extract_code_blocks(doc: Any) -> List[CodeBlock]:
    """Extract code blocks from the document."""
    code_blocks = []

    try:
        codes = getattr(doc, "code_blocks", []) or []
        for idx, code in enumerate(codes):
            cb = CodeBlock(
                content=getattr(code, "content", str(code)) or str(code),
                language=getattr(code, "language", "") or "",
                page_number=getattr(code, "page_no", None),
            )
            code_blocks.append(cb)
    except Exception as e:
        logger.debug(f"Could not extract code blocks: {e}")

    return code_blocks


def extract_equations(doc: Any) -> List[Equation]:
    """Extract mathematical equations from the document."""
    equations = []

    try:
        eqs = getattr(doc, "equations", []) or getattr(doc, "formulas", []) or []
        for eq in eqs:
            equation = Equation(
                content=getattr(eq, "content", str(eq)) or str(eq),
                format=getattr(eq, "format", "latex") or "latex",
                page_number=getattr(eq, "page_no", None),
            )
            equations.append(equation)
    except Exception as e:
        logger.debug(f"Could not extract equations: {e}")

    return equations


# =============================================================================
# STRUCTURED DOCUMENT BUILDING
# =============================================================================

def build_structured_document(
    source_path: Path,
    doc: Any,
    result: Any,
    output_dir: Path,
    extract_images_flag: bool = True
) -> StructuredDocument:
    """
    Build a complete structured document from the Docling output.

    This is the main orchestration function that calls all extraction functions.
    """
    base_name = source_path.stem

    # Extract metadata
    logger.info("Extracting metadata...")
    metadata = extract_metadata(source_path, doc)

    # Build sections and get text blocks
    logger.info("Building document sections...")
    sections, all_blocks = build_sections_from_document(doc)

    # Extract tables
    logger.info("Extracting tables...")
    tables = extract_tables_from_document(doc)

    # Extract images
    figures = []
    if extract_images_flag:
        logger.info("Extracting images...")
        figures = extract_images_from_document(doc, result, output_dir, base_name)

    # Extract other elements
    logger.info("Extracting hyperlinks, code blocks, and equations...")
    hyperlinks = extract_hyperlinks(doc)
    code_blocks = extract_code_blocks(doc)
    equations = extract_equations(doc)

    # Get raw text for fallback/search
    raw_text = ""
    try:
        if hasattr(doc, "export_to_text"):
            raw_text = doc.export_to_text() or ""
        elif hasattr(doc, "text"):
            raw_text = doc.text or ""
    except Exception:
        pass

    # Build footnotes, headers, footers (if available)
    footnotes = []
    headers = []
    footers = []

    try:
        for fn in getattr(doc, "footnotes", []) or []:
            footnotes.append(TextBlock(
                type="footnote",
                content=getattr(fn, "text", str(fn)) or str(fn),
                page_number=getattr(fn, "page_no", None),
            ))
    except Exception:
        pass

    return StructuredDocument(
        metadata=metadata,
        main_text=sections,
        tables=tables,
        figures=figures,
        code_blocks=code_blocks,
        equations=equations,
        hyperlinks=hyperlinks,
        footnotes=footnotes,
        headers=headers,
        footers=footers,
        raw_text=raw_text,
    )


# =============================================================================
# JSON EXPORT
# =============================================================================

def try_export_docling_json(doc: Any) -> Optional[Dict[str, Any]]:
    """
    Try to export el JSON/dict nativo de Docling. Devuelve None si no está disponible.
    """
    exporters = ("export_to_dict", "to_dict", "dict")
    for exporter in exporters:
        try:
            if hasattr(doc, exporter):
                fn = getattr(doc, exporter)
                data = fn()
                if data:
                    return data
        except Exception as e:
            logger.debug(f"Docling JSON export via {exporter} failed: {e}")

    # Último recurso: save_to_json a un archivo temporal
    try:
        if hasattr(doc, "save_to_json"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
                tmp_path = Path(tmp.name)
            doc.save_to_json(str(tmp_path))
            data = json.loads(tmp_path.read_text(encoding="utf-8"))
            tmp_path.unlink(missing_ok=True)
            return data
    except Exception as e:
        logger.debug(f"Docling JSON export via save_to_json failed: {e}")

    return None

def dataclass_to_dict(obj: Any) -> Any:
    """Convert dataclass to dict, handling nested structures."""
    if hasattr(obj, "__dataclass_fields__"):
        return {k: dataclass_to_dict(v) for k, v in asdict(obj).items()}
    elif isinstance(obj, list):
        return [dataclass_to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: dataclass_to_dict(v) for k, v in obj.items()}
    return obj


def export_to_json(
    structured_doc: StructuredDocument,
    output_path: Path,
    native_docling: Optional[Dict[str, Any]] = None
) -> None:
    """
    Export the structured document to a JSON file.

    The JSON format is optimized for LLM parsing with clear structure.
    """
    logger.info(f"Exporting JSON to: {output_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert to dictionary
    doc_dict = dataclass_to_dict(structured_doc)

    # Add schema version for future compatibility
    doc_dict["_schema_version"] = "2.0"
    doc_dict["_format"] = "lossless_structured_document"
    if native_docling:
        try:
            # Asegurar serialización (Docling puede incluir objetos RefItem)
            sanitized = json.loads(json.dumps(native_docling, default=str))
            doc_dict["docling_native"] = sanitized
        except Exception as e:
            logger.debug(f"No se pudo serializar docling_native, se omite: {e}")

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(doc_dict, f, ensure_ascii=False, indent=2, default=str)

    logger.info(f"JSON export complete: {output_path}")


# =============================================================================
# MARKDOWN EXPORT
# =============================================================================

def try_export_docling_markdown(doc: Any) -> Optional[str]:
    """
    Devuelve Markdown nativo de Docling si es posible, o None si falla.
    """
    try:
        try:
            from docling.datamodel.document import ImageRefMode
        except Exception:
            ImageRefMode = None

        if hasattr(doc, "export_to_markdown"):
            if ImageRefMode:
                md = doc.export_to_markdown(image_mode=ImageRefMode.EMBEDDED)
            else:
                md = doc.export_to_markdown()
            if md and md.strip():
                return md

        if hasattr(doc, "save_to_markdown"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp:
                tmp_path = Path(tmp.name)
            # Parámetros variables según versión
            try:
                doc.save_to_markdown(str(tmp_path))
            except TypeError:
                doc.save_to_markdown(tmp_path)
            md = tmp_path.read_text(encoding="utf-8")
            tmp_path.unlink(missing_ok=True)
            if md and md.strip():
                return md
    except Exception as e:
        logger.debug(f"Docling Markdown export failed: {e}")

    return None

def section_to_markdown(section: Section, indent_level: int = 0) -> str:
    """Convert a section to Markdown format."""
    lines = []

    # Add heading
    heading_prefix = "#" * min(section.level + indent_level, 6)
    lines.append(f"{heading_prefix} {section.title}\n")

    # Add content blocks
    for block in section.content:
        if block.type == "paragraph" or "text" in block.type:
            lines.append(f"{block.content}\n")
        elif block.type == "list_item":
            indent = "  " * block.level
            lines.append(f"{indent}- {block.content}")
        elif block.type == "code":
            lines.append(f"```\n{block.content}\n```\n")
        elif block.type == "quote" or "blockquote" in block.type:
            lines.append(f"> {block.content}\n")
        else:
            lines.append(f"{block.content}\n")

    # Add subsections
    for subsection in section.subsections:
        lines.append(section_to_markdown(subsection, indent_level))

    return "\n".join(lines)


def table_to_markdown(table: Table) -> str:
    """Convert a table to Markdown format."""
    lines = []

    if table.caption:
        lines.append(f"**Table: {table.caption}**\n")

    if table.headers:
        lines.append("| " + " | ".join(table.headers) + " |")
        lines.append("| " + " | ".join(["---"] * len(table.headers)) + " |")

        for row in table.rows:
            # Ensure row has same length as headers
            padded_row = row + [""] * (len(table.headers) - len(row))
            lines.append("| " + " | ".join(str(cell) for cell in padded_row[:len(table.headers)]) + " |")
    elif table.rows:
        # No headers, just rows
        if table.rows:
            num_cols = max(len(row) for row in table.rows)
            lines.append("| " + " | ".join([f"Col {i+1}" for i in range(num_cols)]) + " |")
            lines.append("| " + " | ".join(["---"] * num_cols) + " |")
            for row in table.rows:
                padded_row = row + [""] * (num_cols - len(row))
                lines.append("| " + " | ".join(str(cell) for cell in padded_row) + " |")

    return "\n".join(lines) + "\n"


def figure_to_markdown(figure: Figure) -> str:
    """Convert a figure reference to Markdown format."""
    alt_text = figure.alt_text or figure.caption or f"Figure {figure.id}"

    if figure.extraction_error:
        return f"<!-- Image extraction failed: {figure.extraction_error} -->\n[Image: {alt_text}]\n"

    md = f"![{alt_text}]({figure.asset_path})"

    if figure.caption:
        md += f"\n*{figure.caption}*"

    if figure.bounding_box:
        md += f"\n<!-- bbox: {figure.bounding_box} -->"

    return md + "\n"


def export_to_markdown(
    structured_doc: StructuredDocument,
    output_path: Path,
    native_markdown: Optional[str] = None
) -> None:
    """
    Export the structured document to a Markdown file.

    The Markdown is structured with clear sections for easy LLM parsing.
    """
    logger.info(f"Exporting Markdown to: {output_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []

    # Document header with metadata
    lines.append("---")
    lines.append(f"source: {structured_doc.metadata.source_filename}")
    lines.append(f"file_type: {structured_doc.metadata.file_type}")
    if structured_doc.metadata.title:
        lines.append(f"title: {structured_doc.metadata.title}")
    if structured_doc.metadata.author:
        lines.append(f"author: {structured_doc.metadata.author}")
    lines.append(f"ingested: {structured_doc.metadata.ingestion_timestamp}")
    lines.append(f"pages: {structured_doc.metadata.page_count}")
    lines.append(f"words: {structured_doc.metadata.word_count}")
    lines.append("---\n")

    if native_markdown:
        # Usar la salida nativa de Docling (mejor fidelidad)
        lines.append(native_markdown.strip())

        # Añadir activos estructurados que la salida nativa suele omitir (p.ej. figuras)
        if structured_doc.figures:
            lines.append("\n## Figures\n")
            for figure in structured_doc.figures:
                lines.append(figure_to_markdown(figure))

        # Hyperlinks y otros artefactos pueden faltar en el markdown nativo
        if structured_doc.hyperlinks:
            lines.append("\n## Hyperlinks\n")
            for link in structured_doc.hyperlinks:
                lines.append(f"- [{link.text}]({link.url})")
            lines.append("")
    else:
        # Main title
        title = structured_doc.metadata.title or structured_doc.metadata.source_filename
        lines.append(f"# {title}\n")

        # Main text sections
        for section in structured_doc.main_text:
            lines.append(section_to_markdown(section))

        # Tables section
        if structured_doc.tables:
            lines.append("\n## Tables\n")
            for table in structured_doc.tables:
                lines.append(table_to_markdown(table))

        # Figures section
        if structured_doc.figures:
            lines.append("\n## Figures\n")
            for figure in structured_doc.figures:
                lines.append(figure_to_markdown(figure))

        # Code blocks section
        if structured_doc.code_blocks:
            lines.append("\n## Code Blocks\n")
            for code in structured_doc.code_blocks:
                lang = code.language or ""
                lines.append(f"```{lang}\n{code.content}\n```\n")

        # Equations section
        if structured_doc.equations:
            lines.append("\n## Equations\n")
            for eq in structured_doc.equations:
                if eq.format == "latex":
                    lines.append(f"$$\n{eq.content}\n$$\n")
                else:
                    lines.append(f"{eq.content}\n")

        # Hyperlinks section
        if structured_doc.hyperlinks:
            lines.append("\n## Hyperlinks\n")
            for link in structured_doc.hyperlinks:
                lines.append(f"- [{link.text}]({link.url})")
            lines.append("")

        # Footnotes section
        if structured_doc.footnotes:
            lines.append("\n## Footnotes\n")
            for i, fn in enumerate(structured_doc.footnotes, 1):
                lines.append(f"[^{i}]: {fn.content}")
            lines.append("")

    # Write to file
    content = "\n".join(lines)
    output_path.write_text(content, encoding="utf-8")

    logger.info(f"Markdown export complete: {output_path}")


# =============================================================================
# MAIN PROCESSING FUNCTIONS
# =============================================================================

def process_single_file(
    input_path: Path,
    output_json: Optional[Path],
    output_md: Optional[Path],
    extract_images: bool = True
) -> int:
    """
    Process a single document file.

    Returns:
        0 on success, non-zero on failure
    """
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        return 1

    # Determine output directory for assets
    if output_json:
        output_dir = output_json.parent
    elif output_md:
        output_dir = output_md.parent
    else:
        output_dir = Path(".")

    try:
        # Extract document
        doc, result = extract_document(input_path, extract_images)

        # Try native Docling exports (mejor fidelidad)
        native_md = try_export_docling_markdown(doc)
        native_json = try_export_docling_json(doc)

        # Build structured document
        structured_doc = build_structured_document(
            input_path, doc, result, output_dir, extract_images
        )

        # Export outputs
        if output_json:
            export_to_json(structured_doc, output_json, native_json)

        if output_md:
            export_to_markdown(structured_doc, output_md, native_md)

        logger.info(f"Successfully processed: {input_path}")
        return 0

    except Exception as e:
        logger.error(f"Failed to process {input_path}: {e}")
        import traceback
        logger.debug(traceback.format_exc())
        return 1


def process_batch(
    sources_dir: Path,
    output_dir: Path,
    formats: Set[str],
    exts: Set[str],
    recursive: bool,
    extract_images: bool
) -> int:
    """
    Process multiple documents in batch mode.

    Returns:
        0 on success, non-zero if any file failed
    """
    if not sources_dir.exists():
        logger.error(f"Sources directory not found: {sources_dir}")
        return 2

    files = list(iter_sources(sources_dir, exts, recursive))
    if not files:
        logger.warning("No source files found.")
        return 0

    logger.info(f"Found {len(files)} files to process")

    failed = 0
    for src in files:
        rel_path = src.relative_to(sources_dir)

        try:
            # Extract document
            doc, result = extract_document(src, extract_images)

            # Try native exports por mejor fidelidad
            native_md = try_export_docling_markdown(doc)
            native_json = try_export_docling_json(doc)

            # Build structured document
            structured_doc = build_structured_document(
                src, doc, result, output_dir, extract_images
            )

            # Export in requested formats
            if "json" in formats:
                json_path = (output_dir / rel_path).with_suffix(".json")
                export_to_json(structured_doc, json_path, native_json)

            if "md" in formats:
                md_path = (output_dir / rel_path).with_suffix(".md")
                export_to_markdown(structured_doc, md_path, native_md)

            logger.info(f"OK: {src} -> {output_dir}")

        except Exception as e:
            logger.error(f"FAILED: {src} - {e}")
            failed += 1

    if failed:
        logger.warning(f"{failed} file(s) failed to process")
        return 1

    return 0


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main() -> int:
    """Main entry point for the script."""
    args = parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Determine mode: single file or batch
    if args.input:
        # Single file mode
        input_path = Path(args.input)
        output_json = Path(args.output_json) if args.output_json else None
        output_md = Path(args.output_md) if args.output_md else None

        if not output_json and not output_md:
            # Default outputs
            output_json = input_path.with_suffix(".json")
            output_md = input_path.with_suffix(".md")
            logger.info(f"No output paths specified. Using defaults: {output_json}, {output_md}")

        return process_single_file(
            input_path, output_json, output_md, args.extract_images
        )
    else:
        # Batch mode
        sources_dir = Path(args.sources_dir)
        output_dir = Path(args.output_dir)
        exts = normalize_exts(args.ext)
        formats = {p.strip().lower() for p in args.formats.split(",") if p.strip()}

        unknown = formats - VALID_FORMATS
        if unknown:
            logger.error(f"Unsupported formats: {', '.join(sorted(unknown))}")
            return 2

        return process_batch(
            sources_dir, output_dir, formats, exts,
            args.recursive, args.extract_images
        )


if __name__ == "__main__":
    raise SystemExit(main())
