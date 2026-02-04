# Convenciones

## Nomenclatura
- ADR: `ADR-###-titulo-corto.md`
- FR: `FR-###-titulo-corto.md`
- NFR: `NFR-###-titulo-corto.md`
- Actas: `MN-YYYY-MM-DD-tema.md`
- Entregables: `E#.#-nombre.md`
- Ingestados: mismo nombre base y ruta relativa que el archivo en `sources/raw/` con `.md` y `.json`

## Estados
- draft | in-review | approved

## Ingestados
- `ingested/` se genera automáticamente (no edición manual)
- si cambia la fuente, se regenera

## Trazabilidad mínima
Todo documento curado debe indicar:
- id
- owner
- status
- date
- sources (rutas a `sources/raw/` y/o URLs externas)
- si se apoya en `ingested/`, igual debe referenciar la fuente original en `sources/raw/`
