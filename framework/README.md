# ProjectDocsFramework
Framework de Infraestructura como Documentación + PromptOps (Markdown + VSCode)

Framework para **Infraestructura como Documentación + PromptOps**.

## Objetivo
Centralizar el conocimiento de un proyecto en una estructura de documentación usando **Markdown**, con:
- estructura de carpetas estable,
- plantillas estandarizadas,
- playbooks de prompts reutilizables,
- trazabilidad (fuentes → artefactos curados → entregables).

## Qué es / Qué no es
**Es:**
- un framework reusable para aplicar a proyectos.
- un sistema de documentación versionada y auditable.

**No es:**
- el proyecto final.
- un sitio web de documentación (puede exportarse, pero no es el objetivo).

## Estructura (alto nivel)
- `00-manifest/` Principios y convenciones
- `01-structure/` Esqueleto para proyectos
- `02-templates/` Plantillas Markdown
- `03-playbooks/` PromptOps (playbooks)
- `04-workflows/` Operación diaria y procesos

Todo el material de trabajo (fuentes, derivados, curados y entregables) vive dentro de `01-structure/project-skeleton/` para mantener el repo raíz limpio. Evita dejar archivos sueltos en la raíz.

## Cómo aplicarlo a un proyecto (rápido)
1. Copia `01-structure/project-skeleton/` dentro del proyecto.
3. Usa las plantillas de `02-templates/` para crear documentos en `curated/` y `deliverables/`.
4. Estándar de trazabilidad: `00-manifest/conventions.md` + `00-manifest/integrations.md`.
5. Operación diaria: `04-workflows/`.

Atajos:
- `04-workflows/how-to-create-fr.md`
- `04-workflows/how-to-create-adr.md`
- `04-workflows/how-to-publish-deliverable.md`
- `03-playbooks/apply-framework-to-project.md`

## Para LLMs
- Antes de responder, lee este README del framework y el `README.md` de `01-structure/project-skeleton/` para entender la convención.
- Usa los documentos del proyecto (no del framework) que están en `01-structure/project-skeleton/ingested/` como fuente primaria de contexto.

## Estado
- status: draft
- owner: Carlos Zavala
