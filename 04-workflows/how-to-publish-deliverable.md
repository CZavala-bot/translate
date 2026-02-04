# Cómo — Publicar un entregable

## Objetivo
Crear un entregable versionado en `deliverables/` que referencia documentación curada.

## Pasos
1. Define el entregable (qué vas a “formalizar” y para quién).
2. Asegura que los documentos base en `curated/` estén en `approved` (o documenta excepciones).
3. Crea el archivo en `deliverables/` con la nomenclatura: `E#.#-nombre.md`.
4. Copia la plantilla `02-templates/deliverable.md` y rellena los metadatos:
   - `id`, `title`, `version`, `date`, `owner`, `status`
5. En **Referencias**, enlaza los FR/NFR/ADR y otros documentos de `curated/` que sustentan el entregable.
6. Marca `status: approved` cuando esté cerrado y evita editarlo: si cambia, crea una nueva versión.

## Lista de verificación rápida
- el entregable referencia documentos concretos en `curated/`
- se puede responder: “¿qué cambió entre v0.1 y v0.2?”
