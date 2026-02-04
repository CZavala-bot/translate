# sources

Contenedor de fuentes de información.

## Estructura

### `raw/` (Inmutable)
Aquí van los archivos originales tal cual se recibieron ("instantáneas").
- PDFs, contratos, normativas.
- Emails exportados (`.eml`, `.msg`).
- Capturas de pantalla, grabaciones.

> **Regla de oro:** El contenido de `raw/` **nunca se edita**. Si necesitas modificarlo (ej. tachar datos sensibles), crea una copia en otra carpeta (ej. `sources/sanitized/`).

### ¿Por qué no poner los archivos directamente aquí?
Para mantener el orden y permitir otros tipos de fuentes en el futuro, como:
- `sanitized/`: Documentos con datos sensibles ocultos.
- `transcripts/`: Transcripciones manuales de audios.
- `apis/`: Especificaciones OpenAPI/Swagger externas.
