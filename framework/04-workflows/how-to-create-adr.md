# Cómo — Crear un ADR (Registro de decisión de arquitectura)

## Objetivo
Registrar una decisión importante para que sea entendible y auditable en el tiempo.

## Pasos
1. Confirma que aplica: hay alternativas, la decisión no es obvia y revertirla es costoso.
2. Identifica la(s) fuente(s) (ticket, reunión, documento, debate) y añade una instantánea a `sources/raw/` si aplica.
3. Si la fuente es un documento (PDF/DOCX/PPTX, etc.), genera `ingested/` usando `04-workflows/how-to-ingest-sources-docling.md` y úsalo para extraer contexto, alternativas y citas (sin reemplazar `sources:`).
4. Crea el archivo en `curated/` con la nomenclatura: `ADR-###-titulo-corto.md`.
5. Copia la plantilla `02-templates/adr.md` y rellena los metadatos:
   - `id`, `title`, `date`, `owner`, `sources`, `status`
6. Completa el cuerpo:
   - **Contexto**: qué problema resuelve y qué restricciones existen
   - **Decisión**: en una frase clara, sin ambigüedad
   - **Alternativas**: opciones reales consideradas y por qué no se eligieron
   - **Consecuencias**: trade-offs, impacto, riesgos y deuda
7. Enlaza FR/NFR relacionados (en el cuerpo y/o con links explícitos).

## Lista de verificación rápida
- la decisión es explícita (se puede citar)
- hay alternativas consideradas (si aplica)
- si aplica, existe `.md` y `.json` en `ingested/` para la instantánea en `sources/raw/`
- `sources:` permite reconstruir el “por qué” en <2 minutos
