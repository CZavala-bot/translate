---
source: [TRANSLATE] E2.1 Diseño de la base de datos.docx
file_type: .docx
ingested: 2026-02-04T16:02:43.041228
pages: 0
words: 2186
---

<!-- image -->

Código

TRANSLATE – E2.1

Fecha

Abril 2024

Versión

01

<!-- image -->

## 1 Contenido

[1	Introducción	4](.)

[2	Requisitos de la base de datos	5](.)

[2.1	Requisitos funcionales	5](.)

[2.2	Requisitos no funcionales	6](.)

[3	Modelo de datos	8](.)

[3.1	Diagrama general	8](.)

[3.2	Principales tablas	10](.)

[3.3	Relaciones e identificadores	11](.)

[3.4	Aspectos de seguridad	11](.)

[3.5	Medidas de optimización y auditoría	12](.)

[4	Conclusiones	13](.)

## 2 Introducción

La arquitectura general de la plataforma TRANSLATE está diseñada para garantizar la interoperabilidad, eficiencia y seguridad en el intercambio de mensajes entre sistemas del sector logístico-portuario. Para ello, el sistema se compone por tres instancias de bases de datos distintas, cada una con su propósito específico:

1. **Base de datos de TRANSLATE BACK API** :

Gestiona las operaciones de negocio. Reúne la información de clientes y organizaciones, permisos de acceso, el catálogo de integraciones disponibles y la evidencia de uso y cambios. Además, alimenta la web de administración y cliente, y sirve de fuente estable para informes y datos abiertos.

1. **Base de datos de TRANSLATE BACK INTEGRATOR** :

Gestiona la operativa diaria, es decir, qué se recibe, cómo se transforma y a donde se envía. Guarda el estado de las tareas en curso y lo necesario para reintentos y recuperación. Sus datos son instrumentales para que el flujo no se detenga y puedan resolverse incidencias rápidamente.

1. **Base de datos de BLOCKCHAIN** :

Custodia pruebas de que los mensajes existieron y fueron procesados, mediante huellas y sellos de tiempo. No guarda el contenido completo ni se usa para operar. Esta base de datos otorga confianza externa y garantía de integridad verificable del servicio.

Este documento, correspondiente a la segunda entrega del proyecto TRANSLATE, se centra exclusivamente en detallar el diseño de la **base de datos de TRANSLATE BACK API** . En él se abordarán los requisitos funcionales y técnicos, descripción de las entidades y relaciones clave, estrategia de implantación con las tecnologías seleccionadas y las optimizaciones para garantizar escalabilidad, seguridad y rendimiento.

## 3 Requisitos de la base de datos

En este apartado se detallan los requisitos necesarios para garantizar que la base de datos principal de la plataforma TRANSLATE pueda cumplir con sus objetivos de interoperabilidad, eficiencia y seguridad.

### 3.1 Requisitos funcionales

Los requisitos funcionales que afectan directamente al diseño de la base de datos principal de TRANSLATE derivan de las funciones clave de la plataforma, y se organizan de la siguiente manera:

- **Gestión de identidad y accesos:**
    - Multiempresa y multidelegación:
        - Implica la separación lógica por empresa y delegación.
    - Gestión de identidades para autenticación y autorización:
        - Requiere representar usuarios roles y permisos para el control de acceso.
    - Gestión de permisos específicos por modelo de integración y servicio:
        - Conlleva vincular permisos a tipos de mensaje, integraciones y servicios.
    - Autenticación de usuario mediante usuario y contraseña:
        - Exige persistir de forma segura los atributos de autenticación y eventos de acceso.
- **Procesamiento y transformación de mensajes:**
    - Soporte de múltiples formatos estándar:
        - Demanda catalogar formatos y sus versiones de mensaje.
    - Permitir la transformación de mensajes tipo EDIFACT y X12:
        - Supone registrar y versionar reglas de mapeo entre estándares.
    - Procesamiento mensajes en diversos formatos según origen y destino
        - Necesita identificar de forma unívoca origen/destino y el estado de procesamiento del mensaje.
- **Auditoría:**
    - Acceder a la trazabilidad de los mensajes mediante la auditoría:
        - Implica el registro de eventos y cambios relevantes a lo largo del ciclo de vida del mensaje.
- **Integraciones:**
    - Permitir la Integración con sistemas externos para recibir y enviar mensajes:
        - Implica almacenar metadatos de conectividad, entregas y reintentos por integración.
    - Configurar TRANSLATE ADAPTER para facilitar la comunicación segura de empresas con limitaciones:
        - Exige la facilitación de comunicaciones seguras por cliente y por flujo.
- **Información de errores y eventos:**
    - Proporcionar información detallada sobre errores:
        - Precisa una taxonomía de errores vinculada al mensaje, a la etapa y a su causa.
- **Modelo de pago por uso:**
    - Suscripción de los clientes a tipos de mensajes y origen/destino:
        - Define reglas de acceso y consumo por cliente.
    - Cálculo de métricas de uso:
        - Incorpora la captura de eventos mínimos para agregación temporal y por cliente.
- **OpenData**
    - Recolección de datos anonimizados:
        - Asegura procesos de anonimización/seudonimización con trazabilidad de reglas aplicadas.
    - Publicación periódica de datos abiertos:
        - Requiere versionar los datasets publicados con metadatos de periodo y generación.

Estos requisitos funcionales se traducen en estructuras persistentes dentro de la base de datos que permiten operar, auditar, personalizar y escalar la solución conforme a las necesidades del sector logístico-portuario.

### 3.2 Requisitos no funcionales

Los requisitos no funcionales impactan principalmente en cómo se organiza, despliega y protege la base de datos. Aunque no definen directamente entidades o relaciones, condicionan su diseño, rendimiento y sostenibilidad a largo plazo. Se agrupan en:

- **Requisitos de arquitectura**
    - La base de datos se alojará en una plataforma cloud, lo cual influye en decisiones de escalabilidad, disponibilidad y costos (SLA).
    - La integración con Blockchain requiere almacenar referencias y metadatos (hashes, IDs de transacción) para enlazar registros con su traza en la cadena.
    - El uso de contenedores Docker condiciona la configuración y persistencia, backups y redes internas de la base de datos.
    - La interacción con un Message Broker exige registrar estados, logs o referencias cruzadas entre la base de datos y las colas de procesamiento.
- **Requisitos de integración/APIs**
    - El diseño de la base de datos debe acompañar la evolución de las APIs documentadas en Swagger, garantizando consistencia de estructuras y flexibilidad ante cambios de versión.
- **Requisitos de seguridad**
    - Debe contemplar una estrategia robusta de copias de seguridad, restauración y alta disponibilidad.
- **Requisitos de rendimiento**
    - Se debe garantizar alta disponibilidad y escalabilidad horizontal en el entorno cloud.
    - Es necesario optimizar consultas e índices para mejorar los tiempos de respuesta en operaciones críticas.
- **Requisitos de mantenimiento.**
    - La base de datos debe facilitar tareas de monitoreo y diagnóstico mediante registros de errores y trazas operativas.
    - Se deben registrar eventos o fallos de manera estructurada para facilitar su revisión desde las interfaces de usuario.

Estos requisitos no funcionales definen el marco técnico en el que debe operar la base de datos.

## 4 Modelo de datos

Este apartado describe el diseño lógico de la base de datos implementada para **TRANSLATE BACK API** . De detallan sus principales componentes estructurales, incluyendo las tablas, sus campos, las relaciones entre entidades y los mecanismos que aseguran la integridad, rendimiento y seguridad.

### 4.1 Diagrama general

La base de datos de TRANSLATE se ha diseñado en torno a un modelo relacional que da soporte a las funcionalidades clave de la plataforma, como se mencionó en el apartado 2 Requisitos de la base de datos. A continuación, se presenta una vista general del modelo, que resume las entidades principales y sus relaciones.

<!-- image -->

Diagrama  Modelo resumido de la base de datos de TRANSLATE.

El modelo relacional de TRANSLATE se organiza en 4 dominios principales:

- **Audit:** traza cada **fichero/mensaje** procesado y su estado operativo, como en: Audit.AuditState y Audit.AuditFile.
- **Party:** referencia los puntos lógicos de **origen/destino** sobre los que se contextualizan tipos de ficheros y rutas, como PCS, navieras, terminales, etc. en la tabla Party.OriginDestination.
- **Messaging:** define los formatos y tipos de mensaje (Plain, EDI, XML, IFCSUM, etc.) en las tablas Messaging.FileFormat y Messaging.FileType.
- **MessagingFlow:** orquesta **flujos, integraciones y configuraciones** de tipos origen/destino, así como la cola de descargas/reintentos, a través de las tablas MessagingFlow.Flow, MessagingFlow.FileTypeConfiguration, MessagingFlow.Integration, MessagingFlow.IntegrationFileTypeConfiguration y MessagingFlow.DownloadFile.

### 4.2 Principales tablas

A continuación, se describen las tablas principales, ordenadas según su rol dentro de la plataforma:

- **Audit.AuditState:** catálogo de estados operativos. Controla el ciclo de vida de la auditoría.
- **Audit.AuditFile:** bitácora por mensaje/fichero (empresa, origen/destino, tipos, longitudes, recibido/transformado/enviado, fecha y observaciones), con campos de auditoría estandarizados.
- **Messaging.FileFormat:** formatos admitidos (EDI, JSON, XML).
- **Messaging.FileType:** tipos de mensaje/fichero con descripción y acrónimo.
- **Party.OriginDestination:** puntos lógicos de origen/destino contra los que se contextualiza el tipo de fichero. (Usada en vistas y FKs de flujo/conectividad).
- **MessagingFlow.Flow:** catálogo de flujos funcionales (agrupa integraciones por “ruta” lógica).
- **MessagingFlow.FileTypeConfiguration:** contextualiza un tipo y formato en un punto (OriginDetinationID, FileTypeId, FileFormatId) y se le asigna un Code único.
- **MessagingFlow.Integration:** configuración activa por empresa (SecurityCompanyId) que enlaza Flow con OriginId/DestinationId.
- **MessagingFlow.IntegrationFileTypeConfiguration:** une una Integration con la FileTypeConfiguration. Es la unidad operativa de “qué se procesa” en esa integración.
- **MessagingFlow.DownloadFile:** registro de descargas y reintentos por IntegrationFileTypeConfigurationId, con MessageIdentifier, ProcessId, RetryNumber y ErrorDescription.

### 4.3 Relaciones e identificadores

Las entidades principales del modelo mantienen relaciones estructuradas que garantizan la integridad referencial y facilitan la trazabilidad de extremo a extremo y la configuración operativa. A continuación, se detallan las relaciones e identificaciones relevantes:

- **Autid.AuditFile** se vincula con **Audit.AuditState** (estado operativo).
- **MessagingFlow.Integration** se relaciona con **Party.OriginDestination (como OriginId y DestinationId)** y con **MessagingFlow.Flow** (agrupación funcional del circuito).
- **MessagingFlow.IntegrationFileTypeConfiguration** enlaza una **Integration** concreta con la **MessagingFlow.FileTypeConfiguration** correspondiente.
- **MessagingFlow.Transformation** define la conversión entre dos configuraciones de tipo origen y destino de **MessagingFlow.FileTypeConfiguration** . Las mismas reglas de transformación pueden ser reutilizadas por múltiples integraciones y compañías.
- **MessagingFlow.FileTypeConfiguration** actúa como puente entre **Party.OriginDestination, Messaging.FileType** y **Messaging.FileFormat** , contextualizando el tipo/formato en un punto lógico y asignándole un Code único para su referencia en catálogo.
- **Messaging.FileType** y **Messaging.FileFormat** quedan asociados a un contexto concreto a través de **FileTypeConfiguration** , representando el aspecto técnico (formato) y lógico (tipo) de archivo/mensaje.
- **MessagingFlow.DownloadFile** referencia **IntegrationFileTypeConfiguration** y utiliza **IntegrationFileTypeConfigurationId** y **MessageIdentifier** como par clave de reintentos.

Todas las tablas, además de un identificador único Id (PK), incluyen campos de auditoría comunes ( **AuditCreationDate, AuditModificationDate, AuditDeletionDate** ) aportados por el framework interno **Helix6.**

### 4.4 Aspectos de seguridad

La base de datos de TRANSLATE ha sido diseñada con un enfoque proactivo en la seguridad cubriendo tanto la protección de los datos en reposo como en tránsito, junto al control de accesos y la trazabilidad de las acciones realizadas.

- Se almacena de forma segura la información sensible: credenciales, roles, tokens y certificados, utilizando técnicas de cifrado y controles de acceso basados en roles y un Identity Manager.
- La autenticación de usuarios se realiza mediante OAuth 2.0.
- Todos los accesos a la base de datos y modificaciones relevantes quedan registrados gracias al esquema de auditoría integrado en el framework de desarrollo Helix6.
- El uso de **Azure Database for PostgreSQL Flexible Serve** como servicio gestionado permite disponer de cifrado en reposo, backups automáticos y restauración, control de acceso por IP/redes privadas, y conexión cifrada (TLS). Además, PostgreSQL ofrece controles de acceso por roles y opciones de auditoría avanzadas.
- Se contempla el almacenamiento de información relativa a certificados digitales necesarios para verificar la identidad de ciertos clientes o sistemas conectados.

Estos mecanismos aseguran que los datos gestionados por la plataforma se mantengan protegidos frente a accesos no autorizados, manipulaciones indebidas y pérdidas accidentales.

### 4.5 Medidas de optimización y auditoría

El diseño de la base de datos de TRANSLATE incorpora estrategias específicas de optimización para garantizar un rendimiento óptimo en los procesos de consulta, transformación y auditoría. Estas son:

- Se han definido índices primarios **(PRIMARY KEY** ) en todas las tablas para asegurar la unicidad e integridad referencial.
- El uso de claves foráneas ( **FOREIGN KEY** ) permite asegurar la consistencia de las relaciones y optimizar las operaciones **JOIN.**
- Para facilitar el acceso rápido a información histórica o de auditoría, se han incorporado campos estándar como **AuditCreationDate** , **AuditModificationDate** y **AuditDeletionDate** con sus respectivos índices.
- La información de auditoría se aprovecha para alimentar visitas de consulta, exportaciones y funcionalidades de trazabilidad en la interfaz de usuario.

Estas prácticas de optimización están alineadas con los requisitos de rendimiento definidos y garantizan una respuesta eficaz incluso bajo cargas elevadas de procesamiento. Por otra parte, este enfoque asegura que cada operación relevante quede registrada, permitiendo reconstruir el historial de cambios sobre cualquier entidad.

## 5 Conclusiones

El diseño de la base de datos de la plataforma TRANSLATE constituye un componente estratégico fundamental para habilitar una solución interoperable, escalable y segura en el contexto de mensajería entre actores logístico-portuarios. A partir del análisis funcional y técnico realizado, se destacan las siguientes conclusiones clave:

1. **Cobertura funcional y técnica completa.**

La estructura relacional soporta todos los bloques funcionales de la plataforma, incluyendo identidad, mensajería, auditoría y eventos, y cumple con los requisitos definidos para el entorno cloud.

1. **Modelo robusto, trazable y escalable.**

Se ha optado por un diseño modular, con relaciones bien definidas, que facilitan la trazabilidad de los mensajes y la futura evolución del sistema.

1. **Seguridad integrada desde el diseño.**

La gestión de accesos, el cifrado de datos sensibles y los mecanismos de auditoría cumplen con los estándares actuales de seguridad y control.

1. **Optimización orientada al rendimiento.**

El uso de índices y claves foráneas permite un acceso eficiente a los datos y asegura un buen comportamiento bajo carga.

En conjunto, el diseño proporciona una base sólida para la interoperabilidad entre plataformas logísticas, con garantías de trazabilidad, rendimiento y adaptabilidad futura.

## Figures

![Figure fig_0](assets/[TRANSLATE] E2.1 Diseño de la base de datos/fig_0.png)

![Figure fig_1](assets/[TRANSLATE] E2.1 Diseño de la base de datos/fig_1.png)

![Figure fig_2](assets/[TRANSLATE] E2.1 Diseño de la base de datos/fig_2.png)

<!-- Image extraction failed: No image data available -->
[Image: Figure fig_3]
