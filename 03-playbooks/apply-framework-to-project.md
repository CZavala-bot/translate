# Playbook — Aplicar ProjectDocsFramework a un proyecto (punto de entrada único)

Hacer posible que cualquier persona o IA aplique este framework a un proyecto real sin leer varios README.

## Cuándo usarlo
- Día 0 / Día 1 de un proyecto
- Cuando migras documentación dispersa a una estructura trazable
- Cuando quieres un MVP de documentación mínimo en 1–2 semanas

## Entradas (provee lo que puedas)
Obligatorias:
- Nombre del proyecto
- Descripción breve del proyecto (qué se va a construir)
- Objetivo / criterios de éxito (qué significa "terminado" para el piloto)
- Responsables (producto + ingeniería)

Opcionales pero muy recomendadas:
- Fuentes existentes (enlaces + archivos): Jira/Confluence/ADO, PDFs, exportaciones de emails, actas
- Restricciones: cumplimiento, seguridad, rendimiento, disponibilidad
- Partes interesadas y audiencias (interno/externo)
- Fechas límite / hitos

## Reglas del framework (obligatorias)
- La estructura es estricta: `sources/raw/` (instantáneas originales) -> `ingested/` (auto-extraído) -> `curated/` (curado por humanos) -> `deliverables/` (salidas formales).
- Nunca edites originales en `sources/raw/`.
- Nunca edites archivos autogenerados en `ingested/`; regenera en su lugar.
- Todo documento curado en `curated/` DEBE incluir metadatos: `id`, `owner`, `status`, `date`, `sources`.
- `sources:` debe referenciar `sources/raw/...` y/o URLs externas estables.
- Nomenclatura:
  - ADR: `ADR-###-titulo-corto.md`
  - FR: `FR-###-titulo-corto.md`
  - NFR: `NFR-###-titulo-corto.md`
  - Actas: `MN-YYYY-MM-DD-tema.md`
  - Entregables: `E#.#-nombre.md`
- Estado: `draft | in-review | approved`

## Contrato de salida (lo que DEBES producir)
1. Decisión de ubicación:
   - "raíz del proyecto" o "docs/" (elige una y sé consistente).
2. Árbol final de carpetas (lo que existe después de la instalación).
3. Resumen de descubrimiento (hechos vs supuestos):
   - tipo de proyecto, partes interesadas, alcance inicial, riesgos evidentes
4. Un plan concreto de MVP de documentación (1–2 semanas):
   - lista de documentos curados a crear con IDs, nombres de archivo, responsables y fuentes
   - 3-5 FR, 1-3 ADR, 1-3 NFR (según aplique), y 1 entregable
5. Comandos a ejecutar (copiar esqueleto + comando de ingestión).

## Instrucciones para la IA (modo agente)
Actúa como un agente de operaciones de documentación. Sé decisivo, pero no inventes hechos.

Paso 0 — Aclarar solo si estás bloqueado
- Si falta alguna entrada obligatoria, haz como máximo 5 preguntas y detente.
- Si no, continúa y declara supuestos claramente.

Paso 0.5 — Descubrimiento (no inventes hechos)
- Identifica:
  - tipo de proyecto
  - partes interesadas
  - alcance inicial
  - riesgos evidentes
- Separa lo conocido (soportado por fuentes) vs supuestos.

Paso 1 — Elegir ubicación e instalar el esqueleto
- Elige una:
  - Opción A: instalar en la raíz del proyecto
  - Opción B: instalar dentro de `docs/`
- Instala la estructura de esqueleto con estas carpetas de primer nivel:
  - `sources/raw/`
  - `ingested/`
  - `curated/`
  - `deliverables/`

Paso 2 — Recolectar fuentes
- Lista lo que debe guardarse como instantáneas en `sources/raw/` (exportaciones PDF, capturas, contratos, exportaciones de actas).
- Para cada fuente, propone un nombre de archivo estable (evita espacios; incluye fecha cuando aplique).

Paso 3 — Ingestar con Docling (Python)
- Si hay archivos convertibles (pdf/docx/pptx/etc), genera AMBOS formatos:
  - `ingested/<misma-ruta-relativa>.md`
  - `ingested/<misma-ruta-relativa>.json`
- Comando (para ejecutar desde la raíz del proyecto donde existe el esqueleto):
```sh
python3 scripts/ingest_docling.py --sources-dir sources/raw --output-dir ingested --formats md,json
```
- Nota: `ingested/` es material de apoyo; los documentos curados igual deben citar `sources/raw/`.

Paso 4 — Proponer el MVP de documentos curados (solo listar)
- Crea un conjunto mínimo de documentos que responda en <2 minutos:
  - "¿De dónde viene este requisito?"
  - "¿Qué decisión explica esta arquitectura?"
  - "¿Qué entregable lo formaliza, y en qué versión?"
- Entrega una tabla con:
  - Ruta (bajo `curated/` o `deliverables/`)
  - ID
  - Título
  - Responsable
  - Estado (inicia en `draft`)
  - Fuentes (al menos 1)
- Usa las plantillas existentes en `02-templates/` (FR/NFR/ADR/meeting-notes/deliverable).

Paso 5 — Producir el primer entregable (línea base)
- Crea un entregable que referencie el MVP de documentos curados.
- Mantenlo corto y formal (alcance/línea base/definición de terminado para el piloto).

## Lista de verificación de calidad (auto-revisión)
- Todo documento en `curated/` tiene metadatos requeridos.
- Todo documento curado tiene `sources:` apuntando a `sources/raw/...` y/o URLs estables.
- No hay ediciones manuales dentro de `ingested/`.
- IDs y nombres de archivo siguen las reglas de nomenclatura.
- El entregable referencia documentos curados, no al revés.

## Prompt para copiar/pegar (uno solo)
Úsalo con cualquier LLM. Reemplaza los placeholders antes de enviar.

```text
Eres un agente de operaciones de documentación.
Aplica ProjectDocsFramework a mi proyecto sin pedirme leer otros documentos.

Entradas:
- Nombre del proyecto: <...>
- Descripción: <...>
- Objetivo / criterios de éxito (piloto, 1-2 semanas): <...>
- Responsables (producto + ingeniería): <...>
- Fuentes existentes (enlaces + archivos): <...>
- Restricciones (seguridad/cumplimiento/rendimiento/etc): <...>
- Partes interesadas/audiencia: <...>
- Fecha límite/hitos: <...>

Reglas que DEBES seguir:
- Estructura: sources/raw (original) -> ingested (auto-extraído) -> curated (curado por humanos) -> deliverables (formal).
- Nunca edites sources/raw. Nunca edites ingested (regenera).
- Todo documento curado DEBE incluir: id, owner, status, date, sources.
- sources debe referenciar sources/raw/... y/o URLs externas estables.
- Nomenclatura:
  - ADR-###-titulo-corto.md
  - FR-###-titulo-corto.md
  - NFR-###-titulo-corto.md
  - MN-YYYY-MM-DD-tema.md
  - E#.#-nombre.md
- Estado: draft | in-review | approved

Contrato de salida:
1) Elige ubicación (raíz del proyecto o docs/) y muestra el árbol final de carpetas.
2) Lista qué archivos originales deben guardarse en sources/raw con nombres propuestos.
3) Entrega un resumen de descubrimiento: tipo de proyecto, partes interesadas, alcance inicial, riesgos evidentes (hechos vs supuestos).
4) Provee el comando de ingestión con Docling (Python) para generar md y json en ingested/.
5) Propón un MVP de documentación de 1-2 semanas:
   - 3-5 FR, 1-3 ADR, 1-3 NFR (según aplique), y 1 entregable.
   - Entrega una tabla: ruta, id, título, responsable, estado, fuentes.

Si faltan entradas obligatorias, haz como máximo 5 preguntas y detente. No inventes hechos.
```
