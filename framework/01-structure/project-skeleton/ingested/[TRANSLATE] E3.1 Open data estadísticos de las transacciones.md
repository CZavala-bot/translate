---
source: [TRANSLATE] E3.1 Open data estadísticos de las transacciones.docx
file_type: .docx
ingested: 2026-02-04T16:03:44.590257
pages: 0
words: 611
---

<!-- image -->

Código

TRANSLATE – E3.1

Fecha

Septiembre 2024

Versión

01

**Control de versiones**

| VERSIÓN   | FECHA   | DESCRIPCIÓN               |
|-----------|---------|---------------------------|
| 01        |         | Elaboración del documento |
|           |         |                           |
|           |         |                           |
|           |         |                           |

**Aprobación**

## 1 Contenido

[1	Introducción	4](.)

[2	Selección de datos	4](.)

[3	Vista de Base de Datos para OpenData	6](.)

[4	Criterios de agrupación	7](.)

## 2 Introducción

Este documento corresponde al entregable E3.1 del proyecto TRANSLATE. Su propósito es evidenciar el desarrollo técnico realizado para habilitar la aportación de datos estadísticos a iniciativas de Open Data, a partir de los mensajes gestionados por la plataforma.

## 3 Requisitos

En este apartado se detallan los requisitos necesarios para garantizar que la plataforma TRANSLATE pueda cumplir con sus objetivos de Open Data. Estos son:

- **Recolección de datos anonimizados**
    - Los datos publicados no contienen información sensible ni identificadores directos.
    - Los conjuntos de datos cumplen con los criterios de anonimización y agregación.
    - Los usuarios pueden acceder y descargar los datos abiertos desde la web.
    - Se documenta el proceso de anonimización y se audita periódicamente.
- **Publicación periódica de los datos abiertos:**
    - Los datos abiertos se publican y actualizan en la web según la periodicidad establecida.
    - Los conjuntos de datos son accesibles y descargables por cualquier usuario.
    - Se mantienen versiones históricas accesibles.
    - La documentación sobre los datos y el proceso de actualización está disponible y es comprensible.
    - Se audita periódicamente la correcta publicación y actualización de los datos.

## 4 Selección de datos

La elección de los datos publicado como OpenData en TRANSLATE busca aportar valor informativo preservando la confidencialidad. Se publicarán datos agregados de actividad, como periodo, ripo de mensajes y estados, respetando los principios de seguridad y transparencia definidos para este proyecto. Para ello, los campos propuestos son:

- **Periodo:** Mes y año en que se procesó el mensaje en formato YYYY-MM.
- **MessageOwner:** Nombre de la entidad pública (origen o destino) que define el mensaje original o transformado. Si no hay entidad pública se muestra como “Privado”.
- **TipoMensajeOriginal:** Tipo o formato del mensaje original recibido.
- **TipoMensajeTransformado:** Tipo o formato del mensaje resultante después de la transformación.
- **Estado:** Estado del mensaje ( **PEN** = Pendiente, **PRO** = Procesado, **ERR** = Error, **OMT** = Omitted).
- **VolumenMensajes:** Número total de mensajes que coinciden con los criterios agrupados.

## 5 Vista de Base de Datos para OpenData

A continuación, se presenta el script que extraerá los datos en el formato indicado.

WITH Mensajes AS (

SELECT

FORMAT(af.[Date], 'yyyy-MM') AS Periodo,

COALESCE(

CASE

WHEN fnt\_orig.Private = 0 THEN od\_orig.Name

WHEN fnt\_dest.Private = 0 THEN od\_dest.Name

ELSE NULL

END, 'Privado') AS MessageOwner,

af.[OriginFileNameType] AS TipoMensajeOriginal,

af.[DestinationFileNameType] AS TipoMensajeTransformado,

st.[Name] AS Estado

FROM

Audit.AuditFile af

INNER JOIN

Audit.State st ON af.StateId = st.Id

LEFT JOIN

Messaging.FileNameType fnt\_orig ON fnt\_orig.Acronym = af.OriginFileNameType

LEFT JOIN

Messaging.FileNameType fnt\_dest ON fnt\_dest.Acronym = af.DestinationFileNameType

LEFT JOIN

Party.OriginDestination od\_orig ON od\_orig.Id = fnt\_orig.OriginDestinationId AND od\_orig.IsOwnerFile = 1

LEFT JOIN

Party.OriginDestination od\_dest ON od\_dest.Id = fnt\_dest.OriginDestinationId AND od\_dest.IsOwnerFile = 1

WHERE

af.AuditDeletionDate IS NULL

)

SELECT

Periodo,

MessageOwner,

TipoMensajeOriginal,

TipoMensajeTransformado,

Estado,

COUNT(*) AS VolumenMensajes

FROM Mensajes

GROUP BY

Periodo, MessageOwner, TipoMensajeOriginal, TipoMensajeTransformado, Estado;

<!-- image -->

Pantalla   Vista de resultados de OpenData.

## 6 Criterios de agrupación

El volumen de mensajes representa una agrupación de ellos según los siguientes criterios:

- **Periodo:** Agrupa los mensajes por mes-año de procesamiento.
- **MessageOwner:** Agrupa según la entidad pública propietaria del mensaje.
- **TipoMensajeOriginal:** Agrupa por tipo de mensaje recibido.
- **TipoMensajeTransformado:** Agrupa por tipo de mensaje enviado (transformado).
- **Estado:** Agrupa por el estado del mensaje ( **PEN** = Pendiente, **PRO** = Procesado, **ERR** = Error).

## Figures

![Figure fig_0](assets/[TRANSLATE] E3.1 Open data estadísticos de las transacciones/fig_0.png)

![Figure fig_1](assets/[TRANSLATE] E3.1 Open data estadísticos de las transacciones/fig_1.png)

<!-- Image extraction failed: No image data available -->
[Image: Figure fig_2]
