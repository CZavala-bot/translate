# Integraciones (Jira / Confluence / Azure DevOps)

Convenciones para enlazar fuentes externas y mantener trazabilidad consistente.

## Regla base
- Todo documento en `curated/` debe incluir `sources:` con **al menos 1** referencia.
- `sources:` acepta:
  - rutas a archivos dentro de `sources/raw/` (preferible si el contenido puede cambiar o desaparecer)

Ejemplo:
```yaml
sources:
  - sources/raw/MN-2026-01-22-kickoff.pdf
```

## Cuándo guardar una copia en `sources/raw/` (instantánea)
Guarda una copia (PDF/exportación) en `sources/raw/` cuando:
- el contenido pueda editarse sin control (páginas vivas)
- el acceso sea frágil (permisos, licencias, rotación de enlaces)
- sea un “contrato” (SOW, alcance firmado, normativa)

## Nota de seguridad
No pegues tokens, claves ni información sensible en URLs o documentos.
