# Cómo — Ingestar fuentes con Docling

## Objetivo
Generar artefactos derivados en `ingested/` (Markdown y JSON) a partir de `sources/raw/`, sin edición manual.

## Características del script `ingest_docling.py`
- JSON estructurado con secciones, tablas, figuras, código, ecuaciones, hipervínculos
- Extracción de imágenes a `ingested/assets/<basename>/`
- Markdown con metadatos y estructura jerárquica
- Registro detallado y manejo de errores
- Optimizado para análisis por LLMs

## Pasos
1. Coloca los originales en `sources/raw/` con nombres estables.
2. Ejecuta el script de ingestión para generar `.md` y `.json` en `ingested/`.
3. Revisa rápidamente la salida (títulos, tablas, secciones clave) para detectar cortes o errores.
4. Si hay problemas, mejora la fuente (nueva exportación/PDF) y re-ejecuta.
5. Crea/actualiza documentos en `curated/` citando `sources/raw/` y, si ayuda, enlaza `ingested/` en el cuerpo.

## Convenciones
- No edites archivos en `ingested/` a mano; se regeneran.
- Salidas esperadas por fuente:
  - `ingested/<basename>.md`
  - `ingested/<basename>.json`
  - `ingested/assets/<basename>/` (imágenes extraídas)

## Instalación
```sh
pip install -r scripts/requirements-ingest.txt
# o manualmente:
pip install docling pillow
```

## Ejemplos de uso

### Modo lote (procesar directorio completo)
```sh
python3 scripts/ingest_docling.py --sources-dir sources/raw --output-dir ingested --formats md,json
```

### Modo archivo único
```sh
python3 scripts/ingest_docling.py --input sources/raw/documento.pdf --output_json ingested/documento.json --output_md ingested/documento.md
```

### Opciones adicionales
```sh
# Sin extracción de imágenes
python3 scripts/ingest_docling.py --sources-dir sources/raw --output-dir ingested --no-extract-images

# Solo PDFs y DOCX
python3 scripts/ingest_docling.py --sources-dir sources/raw --output-dir ingested --ext pdf,docx

# Modo verbose
python3 scripts/ingest_docling.py --sources-dir sources/raw --output-dir ingested -v
```

## Estructura de salida

### JSON estructurado
```json
{
  "_schema_version": "2.0",
  "metadata": { "source_filename": "...", "title": "...", ... },
  "main_text": [ { "id": "sec_0", "title": "...", "content": [...] } ],
  "tables": [ { "id": "tbl_0", "headers": [...], "rows": [...] } ],
  "figures": [ { "id": "fig_0", "asset_path": "assets/doc/fig_0.png", ... } ],
  "code_blocks": [...],
  "equations": [...],
  "hyperlinks": [...],
  "footnotes": [...]
}
```

### Markdown estructurado
```markdown
---
source: documento.pdf
file_type: .pdf
title: Mi Documento
ingested: 2024-01-15T10:30:00
---

# Mi Documento

## Sección 1
Contenido...

## Tablas
| Col1 | Col2 |
|------|------|
| a    | b    |

## Figuras
![Figura 1](assets/documento/fig_0.png)
```

## Lista de verificación rápida
- existe `.md` y `.json` por cada fuente relevante
- los nombres base coinciden con `sources/raw/`
- `curated/` referencia `sources/raw/`
- imágenes extraídas en `ingested/assets/`
