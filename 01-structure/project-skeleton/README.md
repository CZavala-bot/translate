# Esqueleto de proyecto

Estructura base para proyectos que usan ProjectDocsFramework.

## Uso
Este directorio se copia íntegramente al iniciar un proyecto nuevo.

## Objetivo
Separar claramente:
- información original (`sources/raw/`)
- extracción automatizada (`ingested/`)
- conocimiento curado (`curated/`)
- entregables formales (`deliverables/`)

## Regla
Nada se documenta directamente sin pasar por esta estructura.

## Guía rápida para LLMs
- Lee primero este README y el README raíz del framework para seguir las convenciones.
- Para contexto del proyecto, usa los artefactos en `ingested/` (no modifiques nada allí).
