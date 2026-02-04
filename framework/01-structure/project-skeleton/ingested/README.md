# ingested (dentro de `01-structure/project-skeleton/`)

Salidas automatizadas a partir de `sources/raw/` (misma carpeta `project-skeleton`).

## Nota para LLMs
- Este directorio contiene los documentos específicos del proyecto listos para consulta. Úsalos como contexto antes de generar respuestas.

## Que va aqui
- Markdown generado por Docling (`.md`)
- JSON estructurado generado por Docling (`.json`)
- `assets/` - imágenes y recursos extraídos de los documentos
- otros formatos derivados

## Estructura (relativa a `01-structure/project-skeleton/`)
```
ingested/
├── documento1.md
├── documento1.json
├── documento2.md
├── documento2.json
├── assets/
│   ├── documento1/
│   │   ├── fig_0.png
│   │   └── fig_1.png
│   └── documento2/
│       └── fig_0.png
└── README.md
```

## Regla
No editar manualmente; se regeneran desde `sources/raw/`.

## Script de ingestión
Ver `scripts/ingest_docling.py` o `04-workflows/how-to-ingest-sources-docling.md`.
