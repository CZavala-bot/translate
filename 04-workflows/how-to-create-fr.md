# Cómo — Crear un FR (Requisito funcional)

## Objetivo
Crear un requisito funcional trazable y revisable en `curated/`.

## Pasos
1. Identifica la(s) fuente(s): Jira/Confluence/ADO, email, acta, contrato, etc.
2. Si la fuente es “viva” o frágil, guarda una instantánea en `sources/raw/` (PDF/exportación).
3. Si la fuente es un documento (PDF/DOCX/PPTX, etc.), genera `ingested/` usando `04-workflows/how-to-ingest-sources-docling.md` y úsalo para extraer hechos y criterios (sin reemplazar `sources:`).
4. Crea el archivo en `curated/` con la nomenclatura: `FR-###-titulo-corto.md`.
5. Copia la plantilla `02-templates/fr.md` y rellena los metadatos:
   - `id`, `title`, `date`, `owner`, `sources`, `status`
6. Escribe:
   - **Descripción**: qué hace y para qué
   - **Justificación**: valor para negocio/usuario
   - **Criterios de aceptación**: testables (Dado/Cuando/Entonces)
7. Si el FR depende de una decisión importante, crea/actualiza un ADR y enlázalo.

## Lista de verificación rápida
- `sources:` tiene al menos 1 entrada válida
- si aplica, existe `.md` y `.json` en `ingested/` para la instantánea en `sources/raw/`
- la descripción no mezcla “decisión” con “requisito”
- los criterios de aceptación son verificables (no opiniones)
