---
source: Memoria Técnica Proyecto TRANSLATE 2022 (1).docx
file_type: .docx
ingested: 2026-02-04T15:59:59.088718
pages: 0
words: 23461
---

Plataforma de Servicios de Intercambio de Mensajería Abierta e Interoperable para la Logística Portuaria

**Memoria Técnica Proyecto TRANSLATE**

<!-- image -->

**Contenidos**

[1	Presentación de la persona jurídica	5](.)

[1.1	Breve descripción de la base tecnológica	5](.)

[1.2	Clasificación según los criterios del Anexo I del Reglamento (UE) nº 651/2014 de la Comisión	7](.)

[1.3	Derechos de propiedad intelectual o industrial de los que es titular	8](.)

[2	Descripción y propósito del proyecto	9](.)

[2.1	Contexto y problemática actual	9](.)

[2.2	Solución propuesta	10](.)

[3	Alineamiento del proyecto con las características y requisitos del artículo 6 de las bases	14](.)

[4	Carácter disruptivo e innovador	19](.)

[4.1	Componente innovador tangible	19](.)

[4.2	Tecnología propuesta y reto técnico	19](.)

[4.3	Valor diferencial	20](.)

[5	Impacto del proyecto y grado de implantación práctica	21](.)

[5.1	Impacto en el sector logístico-portuario	21](.)

[5.2	Impacto en la sociedad y en la economía	22](.)

[5.3	Impacto en el medio ambiente	22](.)

[6	Protección de la propiedad industrial	24](.)

[7	Justificación del nivel de madurez tecnológica inicial	25](.)

[7.1	Descripción general de la PoC	25](.)

[7.2	Sistema de integración con Valenciaportpcs y Portic	27](.)

[7.3	Esquema detallado de la PoC	30](.)

[8	Plan para la realización del prototipo en entorno real	34](.)

[8.1	Descripción del demostrador de la plataforma TRANSLATE	34](.)

[8.2	Caso de uso 1: Integración de MSC Consignataria	38](.)

[8.3	Caso de uso 2: Integración de PCS de APV – TRADELENS	39](.)

[8.4	Componentes de la nueva plataforma PaaS TRANSLATE	40](.)

[8.5	Plan de trabajo para el desarrollo de la plataforma y el demostrador	43](.)

[8.6	Compromisos de facilitación	56](.)

[9	Medios y Equipo Emprendedor	58](.)

[9.1	Equipo emprendedor	58](.)

[9.2	Medios y recursos técnicos necesarios	64](.)

[10	Plazo de implementación del proyecto	65](.)

[11	Presupuesto	67](.)

[11.1	Resumen del presupuesto	67](.)

[11.2	Costes de personal	68](.)

[11.3	Costes de investigación contractual y conocimientos técnicos	71](.)

[11.4	Gastos generales	71](.)

[11.5	Gastos en prototipos y pilotos	72](.)

[11.6	Costes indirectos	72](.)

[12	Desglose y justificación de subcontrataciones	73](.)

[13	Certificados de apoyo	74](.)

[14	Plan de Negocio	76](.)

[14.1	Resumen Ejecutivo	76](.)

[14.2	Contenido	78](.)

[14.3	Riesgos y amenazas	87](.)

[15	Dotación de ayuda requerida	90](.)

[16	Plan temporal de pago de la ayuda	91](.)

[17	Compromiso de lanzamiento al mercado	92](.)

[18	Anexo I: Cartas de apoyo	93](.)

## 1 Presentación de la persona jurídica

### 1.1 Breve descripción de la base tecnológica

**Infoport Valencia** (en adelante **Infoport** ) se creó en 1998 en el Puerto de Valencia (España) con la misión de proporcionar soluciones tecnológicas para la gestión portuaria y logística y contribuir a incrementar la competitividad de las empresas del sector logístico portuario utilizando las tecnologías para mejorar la eficiencia en sus procesos y operaciones.

Durante más de 20 años, **Infoport** ha acumulado un capital intelectual compuesto por un equipo profesional con amplia experiencia en diseño, desarrollo y operación de sistemas de información para puertos y conocimientos de los procesos de negocio de la logística portuaria, con un promedio de más de 10 años de experiencia en servicios de tecnologías de la información aplicadas al sector portuario y que comparten los valores de **Infoport** de compromiso con nuestros clientes, orientación al servicio, trabajo en equipo y vocación de innovación tecnológica.

Este capital intelectual se completa con un conjunto de productos y capacidades que convierten a **Infoport** en un proveedor integral de soluciones de TI en la industria logístico-portuaria para clientes del sector público y privado en todas las actividades de la cadena logística, contando entre sus clientes con autoridades portuarias, terminales, navieras, consignatarias, transitarías, agentes de aduanas, transportistas terrestres, sociedades de estiba o empresas de servicios técnico-náuticos.

**Infoport** ha ejecutado más de 100 proyectos de tecnologías de la información en puertos de Europa y América con elevados volúmenes de tráfico y niveles de exigencia, entre los que se incluyen proyectos de desarrollo e implantación de sistemas de gestión portuaria, comunidades portuarias, operaciones, servicios técnico-náuticos, transporte intermodal y logística portuaria.

En 2009, el Puerto de Valencia (Valenciaport) fue reconocido con el galardón de “Best in class Port Cluster” concedido a los mejores puertos del mundo. El Puerto de Valencia es actualmente el primer puerto en el Mediterráneo y el cuarto en Europa en el transporte marítimo de contenedores, con un movimiento de 5,6 millones de TEU en 2021 y un crecimiento del 3,4 % en el último año, afianzando su liderazgo entre los puertos del sur de Europa y su posición entre los mayores puertos del mundo. En ambos casos las capacidades de sus sistemas de información, en los que **Infoport** ha sido protagonista del desarrollo, evolución y operación, fueron instrumentos clave en la obtención de estos hitos.

**Infoport** proporciona servicios de consultoría tecnológica, diseño y desarrollo de sistemas de gestión, explotación técnica, planificación y operación de sistemas e infraestructuras de tecnologías de la información.

La empresa también mantiene una línea de negocio dedicada a proyectos de automatización y control en entornos portuarios y un equipo de I+D+i para el desarrollo de todo tipo de proyectos de innovación tecnológica aplicados al ámbito de la logística portuaria.

Nuestros equipos técnicos crean soluciones, arquitecturas, plataformas y frameworks a partir de distintas tecnologías con un modelo de producción de software especializado.

Nuestros servicios incluyen el diseño y desarrollo de la solución, gestión de proyectos y oficinas técnicas, mantenimiento de aplicaciones e integración de sistemas, proporcionando a nuestros clientes un servicio integral que da cobertura al ciclo de vida completo de las aplicaciones.

<!-- image -->

En el ámbito de los sistemas **Infoport** ofrece servicios de explotación técnica, soporte, implantación, modernización y migración tecnológica de infraestructuras y comunicaciones, así como servicios de mejora continua de sistemas y plataformas tecnológicas.

La vocación de innovación tecnológica de **Infoport** ha impulsado a la empresa a liderar y participar de forma continua en proyectos de I+D+i que tienen como objetivo el desarrollo e implantación de nuevas tecnologías en el ámbito logístico y portuario. Algunos de estos proyectos han sido financiados por organismos públicos europeos, nacionales y regionales.

Los procesos y metodologías de gestión de servicios de **Infoport** están basados en los estándares internacionales de calidad y mejores prácticas de servicios de TI y acreditados con las siguientes certificaciones:

- ISO 20000 Sistema de gestión de servicios de tecnologías de la información
- ISO 27001 Sistema de gestión de seguridad de la información
- ISO 9001 Sistema de gestión de la calidad
- ISO 14001 Sistema de gestión medioambiental
- Esquema Nacional de Seguridad (ENS)
- Microsoft Gold Certified Partner

El equipo de proyectos de **Infoport** está certificado en las principales metodologías de desarrollo y gestión de proyectos de tecnologías de la información (PMP, Prince2, Scrum), lo que les permite aplicar las mejores prácticas en nuestros proyectos y servicios.

### 1.2 Clasificación según los criterios del Anexo I del Reglamento (UE) nº 651/2014 de la Comisión

Según los criterios establecidos en el Anexo I del Reglamento (UE) nº 651/2014 de la CE, Infoport se clasifica como **MEDIANA** empresa, atendiendo a que:

- Se trata de una empresa autónoma, puesto que no puede calificarse ni como empresa asociada, ni como empresa vinculada.
- Como empresa autónoma, los datos, incluidos los efectivos, se determinan únicamente sobre la base de las cuentas de Infoport.
- Los efectivos, en número de unidades de trabajo anual (UTA), no exceden de las 250 personas.
- Los límites financieros correspondientes al último ejercicio contable cerrado no exceden de 50 millones EUR en volumen de negocios ni de 43 millones EUR en el balance general anual.

Los accionistas de Infoport son los siguientes:

| Socio                                                      | Porcentaje de participación   |
|------------------------------------------------------------|-------------------------------|
| Autoridad Portuaria de Valencia                            | 24,98%                        |
| Asociación Naviera Valenciana                              | 21,15%                        |
| Prosertek S.A.                                             | 20,00%                        |
| Colegio de Agentes de Aduanas de la Comunidad Valenciana   | 13,87%                        |
| Sociedad Ibérica de Construcciones Eléctricas, S.A. (SICE) | 6,67%                         |
| ATEIA Valencia                                             | 6,67%                         |
| Federación Valenciana de Empresas de Transporte (FVET)     | 6,67%                         |

### 1.3 Derechos de propiedad intelectual o industrial de los que es titular

Infoport no es titular de derechos de propiedad/industrial relevantes para el proyecto TRANSLATE.

## 2 Descripción y propósito del proyecto

### 2.1 Contexto y problemática actual

La modernización tecnológica para el desarrollo del sistema portuario implica la digitalización de sus procesos. El desarrollo y puesta de marcha de sistemas como los **Port Community System (PCS)** por parte de las autoridades portuarias están siendo una de las principales palancas de apoyo en el proceso de digitalización y optimización de procesos de la cadena logístico-portuaria. Los sistemas PCS son, por tanto, una pieza importante en la digitalización de procesos y servicios mediante el intercambio electrónico de información. Asimismo, en los últimos años se han puesto en marcha nuevos servicios e iniciativas de intercambio electrónico, como son la Ventanilla Única Aduanera (VUA) de la AEAT que permite, entre otras cuestiones, centralizar la información y la documentación remitida por los operadores económicos a las distintas autoridades relacionadas con el comercio exterior, la Ventanilla Única Marítimo-Portuaria (DUEPORT) de Puertos del Estado para las escalas de buque, y la plataforma SIMPLE, que integrará toda la información de la actividad del transporte de mercancías y la logística en España.

Por su parte, el Reglamento (UE) 2020/1056 del Parlamento Europeo y del Consejo, de 15 de julio de 2020, sobre información electrónica relativa al transporte de mercancías (e-FTI), tiene el objetivo de apoyar la transformación digital del sector del transporte y la logística, con el fin de conseguir un transporte sin papeles, eliminando la necesidad de documentos en papel en el transporte de mercancías como prueba del cumplimiento de los requisitos legales, mejorar la visibilidad en toda la cadena de suministro, a través de estándares para el intercambio de datos de transporte de mercancías B2A alineados con los principales estándares e iniciativas B2B y complementar otros instrumentos de simplificación del comercio y el transporte de la UE, como la interoperabilidad con las aduanas electrónicas (e-customs) y el entorno de ventanilla única marítima europea (EMSWe).

Sin embargo, la puesta en marcha de estas plataformas digitales requiere de adaptaciones por parte de los operadores económicos interesados, para permitir la interconexión e interoperabilidad de sus sistemas con las mismas. Para integrarse y utilizar de un modo eficiente los servicios proporcionados por dichas plataformas, los operadores económicos tienen que transformar y adaptar los mensajes electrónicos del formato original generado por sus sistemas de información a los formatos esperados por las distintas plataformas. Esta interoperabilidad es uno de los retos para el éxito de las plataformas digitales. Como ejemplo, un consignatario o transitario que opere con tres puertos españoles como pueden ser Valencia, Barcelona y Algeciras, cada uno con su propia plataforma PCS, tiene que transformar los mensajes del formato de sus sistemas internos a cada uno de los formatos de las plataformas PCS con las que opera. Por tanto, aunque todas ellas están basadas en estándares, los trabajos de integración son específicos para cada plataforma destino.

Los recursos técnicos para realizar las integraciones y adaptaciones a los cambios de los sistemas recaen en el propio operador económico o en sus proveedores. Estas adaptaciones en sus sistemas de información generan, en muchas ocasiones, dificultades para las empresas usuarias que, o bien no disponen de las herramientas o medios para implementarlas o, en otros casos, no disponen de los conocimientos técnicos o funcionales necesarios. En cualquier caso, la complejidad y la necesidad de disponer de un conocimiento exhaustivo de las distintas plataformas y herramientas de integración los convierten en procesos costosos de implementar y mantener.

<!-- image -->

Situación actual: los operadores necesitan asegurar la interoperabilidad de sus sistemas con distintas plataformas digitales

### 2.2 Solución propuesta

El propósito del proyecto TRANSLATE es proporcionar un servicio que facilite a los operadores económicos la interconexión e interoperabilidad de sus sistemas de información con las diferentes plataformas de intercambio electrónico del sistema portuario, de un modo transparente y con capacidades de valor añadido. Por tanto, TRANSLATE ofrecerá a los operadores económicos una solución que, desde la perspectiva del operador, permita evitar la complejidad de interconectar sus sistemas con cada una de las plataformas.

El objetivo del proyecto TRANSLATE es centralizar en un único sistema en la nube, a modo de pasarela, la gestión de esos envíos y recepciones de mensajes, con el fin de aumentar el control, minimizar los errores, facilitar la trazabilidad y simplificar la gestión.

El proyecto consiste en una **Plataforma como Servicio (PaaS)** en la nube que unifica los diferentes componentes de mensajería actualmente existentes y que suelen formar parte de desarrollos específicos para cada operador y, además, en cada una de sus respectivas aplicaciones. La plataforma PaaS permitirá gestionar desde un único entorno múltiples formatos de mensajes de diferentes orígenes y con distintos destinos. Además, la plataforma permitirá realizar las transformaciones oportunas de modo que, con independencia del formato del mensaje de origen, el destinatario lo reciba en el formato solicitado.

La plataforma TRANSLATE será en una **solución multiempresa y multiplataforma** que integre los diferentes servicios de mensajería portuaria, basada en las últimas tecnologías en cuanto a componentes software, almacenamiento de datos, procesamiento en la nube y gestión y monetización de Interfases de Integración de Aplicaciones, soportado en 24x7 y atendido con personal experto, tanto en tecnologías como en los procesos y mensajería portuaria.

TRANSLATE permitirá a los propietarios de las plataformas (Autoridades Portuarias, Puertos del Estado, etc.) ofrecer a sus usuarios soluciones para facilitar su adhesión a las plataformas y aumentar la eficiencia de sus operaciones reduciendo el *time-to-market* necesario para integrarse y adaptarse a los cambios continuos. Por otro lado, permitirá a los operadores económicos externalizar servicios de desarrollo y mantenimiento de integraciones que no forman parte del *core* de su negocio y, sin embargo, son necesarios para lograr la digitalización de procesos de la cadena logística y el máximo aprovechamiento de las capacidades que ofrecen las plataformas digitales.

Los operadores económicos y las Autoridades Portuarias dispondrán de una solución, que, entregada como servicio en la nube, redunde en simplificar los desarrollos específicos realizados por cada empresa, ayude a “normalizar” estructuras de intercambio y aprovechar soluciones aplicables a más actores del sector, evitando el desarrollo y mantenimiento por cada empresa y cada aplicación. Se constituiría como un **Hub de Integración Digital (HID)** de los distintos puertos a nivel nacional, así como de otras plataformas de comunicación, constituido además como un servicio en la nube.

<!-- image -->

TRANSLATE facilita la interconexión entre operadores y plataformas digitales

Asimismo, TRANSLATE facilita la interconexión entre plataformas digitales, permitiendo a los usuarios de una plataforma digital enviar y recibir información de otras plataformas digitales con las que los propietarios de la plataforma digital tengan acuerdos de intercambio de información o en las que el operador esté interesado en integrarse.

<!-- image -->

TRANSLATE facilita la interconexión entre plataformas digitales

La plataforma TRANSLATE se ha concebido de forma **totalmente escalable** , tanto en capacidad de los sistemas de información como en los servicios, a medida que se desarrolle el negocio con la incorporación de nuevos operadores económicos, nuevas plataformas digitales y nuevos servicios de las plataformas existentes.

Los beneficiarios del proyecto son:

- Autoridades Portuarias: como proveedores de servicios digitales a su comunidad portuaria, Translate les ofrece una herramienta que facilita la interoperabilidad entre los sistemas de los operadores de la comunidad portuaria con las plataformas de comunidad logística o Port Community Systems.
- Proveedores de plataformas digitales de servicios logísticos: Translate facilita la adhesión a sus plataformas de operadores privados y entidades públicas, minimizando los costes y esfuerzo requeridos para integrarse en estas plataformas.
- Cualquier operador logístico que pueda ser usuario de una plataforma digital logístico-portuaria que permita la integración con sus sistemas mediante mensajería electrónica. A los operadores que no dispone de recursos y medios técnicos para desarrollar la integración de sus sistemas con estas plataformas, Translate les ofrece una alternativa ágil y adaptada a sus necesidades, que les permite conectar con múltiples plataformas locales, nacionales o globales y ofrecer servicios de valor añadido a sus clientes.

En la siguiente tabla se muestra un resumen de los objetivos generales del proyecto TRANSLATE y su relación con los resultados tangibles que se espera obtener una vez desarrollado el prototipo en entorno real:

| Objetivo                                                | Resultado                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Plataforma como servicio en la nube (Paas)              | Disponer de una plataforma como servicio que unifica los diferentes componentes de mensajería actualmente existentes.                                                                                                                                                                                                                                                                                                               |
| Hub de Integración digital (HID)                        | - Integración con PCS de APV (ValenciaPortPCS) - Integración con PCS de APB (PORTIC) - Plataforma configurable para múltiples empresas y delegaciones. - Diseño orientado a la interoperabilidad con diversas plataformas de intercambio electrónico. - La plataforma permite crecer en servicios de interoperabilidad ofrecidos a la comunidad portuaria. - Como usuarios de un mismo servicio pueden existir múltiples entidades. |
| Solución multiempresa y multiplataforma                 |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Plataforma escalable                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Facilitar las integraciones a los operadores económicos | KPI medible del ahorro en tiempo y costes de desarrollo a los operadores económicos.                                                                                                                                                                                                                                                                                                                                                |

## 3 Alineamiento del proyecto con las características y requisitos del artículo 6 de las bases

A continuación, se indica, a modo de referencia que ayude a la comprensión de nuestra propuesta, la correspondencia entre los requisitos del artículo 6 de las bases de “Puertos 4.0”, y la justificación de los motivos por el que el proyecto TRANSLATE está alineado con ellos:

1. **Desarrollar un nuevo producto, servicio o proceso o mejorar una tecnología ya existente con componente innovador y desarrollar su aplicación al sector logístico portuario.**

El proyecto planteado supone la creación de un nuevo servicio de interoperabilidad para la mensajería, mejorando las soluciones actuales al aplicar tecnologías de computación en la nube y un nuevo modelo de negocio de provisión de servicio ( *Service Provisioning)* , inexistente en la actualidad y cuya aplicación supone una mejora importante para muchos actores del sector logístico portuario puesto que se genera economía de escala, evitando los desarrollos y adaptaciones propias de cada entidad ante la aparición de una nueva necesidad y/o modificación de las existentes. La ventaja principal es disponer de una Plataforma como Servicio para poder hacer uso de la conectividad y mensajes que se requieran en cada momento, sin requerir la adaptación particular e independiente de cada parte.

1. **Promover la consecución de soluciones de avance medibles en una o varias de las siguientes áreas de actividad logístico-portuaria:**

TRANSLATE supondrá un impacto positivo en las siguientes áreas:

1. **Eficiencia logística en el ámbito infraestructural, operacional o de prestación de servicios:**

**9.º Promoción y potenciación del transporte multimodal.**

TRANSLATE tiene como objetivo facilitar la interoperabilidad de los sistemas de las empresas de la cadena logística entre sí a través de las plataformas de intercambio electrónico. Parte de los servicios de estas plataformas están orientados a la gestión del transporte en los nodos multimodales que constituyen los puertos.

La reducción en los tiempos de puesta en marcha y la funcionalidad proporcionada mejorarán sustancialmente la eficiencia operacional de estas empresas.

La digitalización de procesos que permite TRANSLATE permite la mejora de eficiencia de la cadena logística reduciendo los tiempos de proceso, en particular en los nodos intermodales donde se producen los intercambios en el medio de transporte de las mercancías y equipamientos como son los puertos, las terminales marítimas y ferroviarias, o los depósitos y almacenes logísticos, entre otros.

Facilitar a través de TRANSLATE el acceso a los servicios de transporte terrestre ofrecidos por los PCS, permitirá obtener una la mejora de indicadores del transporte por carretera, evitan desplazamientos innecesarios y promoviendo la sincronización de todos los agentes de la cadena en beneficio del resultado global. La reducción de los tiempos de desplazamiento y tránsito tiene como consecuencia adicional la reducción de riesgos asociados al transporte.

**13.º Sistemas de trazabilidad en la cadena logística.**

TRANSLATE facilitará la incorporación de las empresas a las plataformas de mensajería del sector logístico-portuario, proporcionando elementos de integración, control, auditoría y trazabilidad de sus transacciones. TRANSLATE pondrá a disposición de los operadores herramientas que les permitirán monitorizar y realizar un seguimiento de los mensajes intercambiados, obteniendo información asociada a sus envíos, como incidencias, desviaciones o eficiencia de los procesos logísticos.

1. **Digitalización de procesos y plataformas inteligentes:**

**1.º Plataformas digitales de gestión e intercambio de datos entre agentes de la comunidad logístico-portuaria (extensión o evolución de sistemas actuales de ventanilla única y gestión de servicios tales como DUEPORT, PCS, eMSWE y otros).**

TRANSLATE tiene como objetivo la conexión digital de la comunidad logístico-portuaria, facilitando los mecanismos de integración entre las plataformas disponibles por las autoridades portuarias y sistemas de mensajería existentes. TRANSLATE parte de la experiencia previa con productos de integración implantados en corporaciones conectadas con numerosos puertos y proporciona una comunidad portuaria conectada. TRANSLATE es capaz de reaprovechar procesos de integración implantados entre una empresa y una plataforma digital de intercambio de información (PCS, VUA, DUEPORT) para poder incorporar nuevas empresas siguiendo parámetros similares.

**5.º Procesos inclusivos de registro y aseguramiento de la fiabilidad y transparencia de la información («blockchain», etc.). Habilitadores digitales.**

La plataforma hará uso de la tecnología blockchain para garantizar la auditabilidad y trazabilidad de la información transmitida. Mediante blockchain como tecnología habilitadora, será posible aprovechar e incorporar a la plataforma TRANSLATE las ventajas de transparencia, inmutabilidad de las transacciones, seguridad y consenso que aporta esta tecnología.

**6.º Puerto info-conectado.**

TRANSLATE aportará un valor diferencial que permitirá la rápida incorporación de nuevos operadores económicos a los procesos integrados de intercambio electrónico, proporcionando un incremento en la calidad y cantidad de la información suministrada a las plataformas logístico-portuarias, reduciendo errores y permitiendo una mayor trazabilidad en la cadena logística.

**7.º Productos que contribuyen a la economía 4.0.**

La introducción de la comunicación automatizada de información de los procesos logísticos empresariales a través de los sistemas de intercambio electrónico, a la que TRANSLATE contribuye, incide directamente en una mayor eficiencia de la cadena logística, anticipa información para la toma de decisiones y reduce riesgos para todos los operadores involucrados, impulsando la economía 4.0 en todo el sector.

1. **Poseer una componente innovadora cierta, demostrable y claramente delimitada al menos en lo que se refiere a su alcance, contenidos y costes, así como no existente en el mercado tanto a nivel nacional como internacional su aplicación para el sector logístico-portuario.**

TRANSLATE proporciona una solución totalmente novedosa en el mercado, estableciendo una interface única de integración de pago por uso entre agentes y las plataformas digitales de intercambio de información, que proporciona elementos de control, auditoría, notificación y trazabilidad de los procesos de integración de una empresa con una o varias plataformas digitales de intercambio de información. Hasta la fecha, debida a la falta de coordinación entre estas plataformas y la falta de estandarización de los procesos en los puertos ha supuesto, en la mayoría de los casos, que las integraciones entre estas y las empresas ha dependido de desarrollos específicos a realizar por el operador para cada puerto y/o servicios de una manera diferente y en la mayoría de los casos sin posibilidad de reutilización. Las labores de integración han supuesto a las empresas subcontratar o disponer de los recursos de personal y equipos especializados para llevar a cabo estas integraciones, suponiendo un alto coste en sus labores de ejecución, desarrollo, mantenimiento y explotación. Adicionalmente, los cambios regulatorios, normativos o de negocio suponen adecuaciones constantes de estas integraciones y repercute en la efectividad de los procesos y en los costes de las empresas.

1. **Poder ser puesto a disposición, y ser testado, implantado o desplegado en uno o más agentes de la comunidad logístico-portuaria.**

El demostrador operacional de TRANSLATE, será probado y puesto a disposición de los agentes facilitadores del proyecto, la **Autoridad Portuaria de Valencia (APV) y Mediterranean Shipping Company (MSC)** , tal como se describe en el *apartado 0 del*

*Plan para la realización del prototipo en* entorno real

1. **Demostrar los resultados de las anteriores fases alcanzadas en el caso de tratarse de productos o servicios con un grado de madurez consolidado.**

TRANSLATE parte de una prueba de concepto inicial con un grado de madurez tecnológica TRL 5, tal como se detalla en el *apartado 7 Justificación del nivel de madurez tecnológica inicial* . El resultado esperado, gracias al desarrollo del proyecto, es la validación de la plataforma en un entorno real logístico-portuario, llegando al nivel TRL 7 de madurez tecnológica.

1. **Preservar, desarrollar o completar los ejes prioritarios y líneas de actuación de la Estrategia Española de Ciencia e Innovación 2013-2020.**

El proyecto TRANSLATE, tal como se plantea y detalla en la presente memoria técnica, está alineado con las líneas de actuación de la Estrategia Española de Ciencia e Innovación:

- Definición de un Entorno Favorable que facilite el desarrollo de las actividades de I+D+i y permita la creación de un marco flexible y eficiente tanto en el ámbito de la I+D pública como empresarial y adaptado a las necesidades de los agentes.

El proyecto de innovación se basa en necesidades reales de los agentes del ecosistema portuario y pretende contar con financiación tanto pública como privada (fondos propios), para ser puesto en el mercado.

- Impulso a la Especialización y Agregación en la Generación de Conocimiento y Talento que promueva una clara división de funciones entre los agentes para facilitar el liderazgo internacional en I+D+i y potencie la complementariedad de las actividades que se desarrollan en los distintos niveles eliminando las ineficiencias asociadas a la redundancia y falta de especialización.

Infoport cuenta con los conocimientos especializados necesarios para el desarrollo de la parte principal del proyecto. No obstante, cuando se requiera un apoyo experto en determinadas tecnologías, por ejemplo blockchain, se recurrirá a empresas especializadas.

- Estímulo a la Transferencia y Gestión del Conocimiento en entornos abiertos y flexibles de colaboración en I+D+i en los que la interacción, la difusión de ideas, y la adopción de objetivos y modelos compartidos favorezca el desarrollo de nuevas ideas e incentive su traslación a novedosas aplicaciones tanto comerciales como no comerciales que permitan mejorar los resultados obtenidos.

El apoyo de los agentes facilitadores, tanto en conocimiento como en recursos, será fundamental para conseguir el objetivo de que la nueva plataforma consiga unos resultados óptimos. Adicionalmente, los resultados del proyecto tendrán una amplia difusión por medio de publicaciones, conferencias, eventos… así como la puesta a disposición de la comunidad de datos abiertos de la plataforma.

- Apoyo a la Internacionalización y promoción del Liderazgo Internacional del Sistema Español de Ciencia, Tecnología e Innovación ya que constituyen un claro factor de competitividad y diferenciación que es necesario potenciar.

Aunque en una primera fase el alcance del proyecto tendrá un ámbito nacional, el objetivo a medio y largo plazo es su internacionalización, tanto en nuevos operadores de otros mercados (principalmente Latinoamérica), como multinacionales que operan en España y terceros países.

- Definición de un marco regional altamente competitivo basado en la Especialización Inteligente de los Territorios que permita vertebrar, en las distintas Comunidades Autónomas, el desarrollo social y económico necesario para favorecer la convergencia a partir de las capacidades del tejido productivo existentes, el potencial científico de sus agentes y el impulso a la innovación como motor del cambio y del progreso.

El desarrollo inicial del proyecto tendrá lugar en la Comunidad Valenciana, con agentes facilitadores del clúster portuario de Valencia, cuyas empresas serán las que de forma más inmediata puedan beneficiarse de los resultados.

- La difusión de una Cultura Científica, Innovadora y Emprendedora que permee en el conjunto de la sociedad, fomente la creatividad e impulse un mayor grado de aceptación social e institucional del emprendimiento.

El proyecto contará con una amplia difusión en múltiples foros y por diferentes medios.

1. **Proporcionar un impacto social favorable sobre el entorno logístico-portuario, sobre el empleo directo o indirecto, y en consecuencia sobre el desarrollo económico y social de los entornos logísticos-portuarios.**

TRANSLATE contribuirá al desarrollo económico y social con la creación de empleo directo e indirecto de calidad a través del mayor grado de digitalización de la actividad de los operadores económicos, que influye directamente en la competitividad de las empresas del sector, tal como se desarrolla en el *apartado 5 Impacto del proyecto y grado de implantación práctica* .

1. **Alcanzar o superar el valor total de los costes asociados a la componente de innovación del proyecto el 50% del presupuesto total de dicho proyecto, aunque tal porcentaje exceda de los límites de financiación establecidos para cada tipo de proyecto en las presentes bases.**

Tal y como se detalla en el *apartado 11 Presupuesto* y se justifica en la descripción del plan de trabajo, el 100% del presupuesto total del proyecto TRANSLATE corresponde al desarrollo de la componente innovadora.

## 4 Carácter disruptivo e innovador

### 4.1 Componente innovador tangible

La plataforma TRANSLATE constituye un elemento innovador cierto como facilitador de la interoperabilidad con las plataformas logísticas de intercambio electrónico, por los siguientes motivos:

- No existe ninguna plataforma ni servicio **orientado a los operadores económicos** que permita la interoperabilidad mediante un punto de acceso único a modo de *hub* con las diferentes plataformas de intercambio electrónico (B2A, B2B), de forma que se simplifiquen las adaptaciones y cambios en la mensajería por parte de los operadores para adaptarse a los requisitos de las plataformas.
- Se trata de un servicio asimilable por cualquier tipo y tamaño de empresa, desde las micropymes hasta las grandes empresas, debido a su flexibilidad y versatilidad, ya que permite interoperar **a partir de cualquier formato o fuente de información** , lo que contribuye al incremento de la digitalización del sector logístico-portuario.
- La plataforma es **escalable tanto a nivel nacional como internacional** , no teniendo límite en las posibilidades de crecimiento, ya que es posible incorporar nuevas plataformas de cualquier puerto con el que trabajen los operadores multinacionales.

### 4.2 Tecnología propuesta y reto técnico

Todas las decisiones tecnológicas de este proyecto están orientadas a que la plataforma TRANSLATE permita:

- Probar e implementar nuevos modelos de integración y transformaciones de forma agil
- Ubicarse en cualquiera de las plataformas cloud existentes
- Crecer y ajustarse según las necesidades de volumen de sus transacciones
- Un despliegue sencillo facilitando su evolución

Todo ello nos ha llevado a la decisión de utilizar **tecnología Docker** . Docker es una plataforma de software que le permite crear, probar e implementar aplicaciones rápidamente. Docker empaqueta software en unidades estandarizadas llamadas [contenedores](https:\aws.amazon.com\es\containers) que incluyen todo lo necesario para que el software se ejecute, incluidas bibliotecas, herramientas de sistema, código y tiempo de ejecución. Con Docker, puede implementar y ajustar la escala de aplicaciones rápidamente en cualquier entorno con la certeza de saber que el código se ejecutará.

El reto que supone el uso de Docker implica que cada uno de los componentes definidos en la arquitectura, encapsulado en un Docker, tiene que ser independiente de los demás, integrable y escalable. Esto supone un cambio significativo a la hora de diseñar la arquitectura y a la hora de realizar los desarrollos de una forma totalmente desacoplada.

Por otro lado, el uso de la **tecnología blockchain** como parte de la solución vendrá a garantizar un nivel alto de confiabilidad en las transacciones, permitiendo utilizar la criptografía para mantener la información segura, proporcionando una base de datos descentralizada para el registro de los mensajes intercambiados.

### 4.3 Valor diferencial

La plataforma global de integración propuesta aporta un valor diferencial que se evidencia por los siguientes aspectos:

- Los operadores económicos no requieren realizar adaptaciones en sus sistemas de información, más allá de las estrictamente necesarias para proporcionar la información requerida por las diferentes plataformas.
- Se concentra en el *hub* la problemática de la integración de mensajes con cada plataforma, evitando el desarrollo específico desde cero por parte de los operadores con cada sistema con el que requiera la conectividad.
- Se genera economía de escala y se concentra cualquier ajuste necesario en un único punto de servicio, que se consume en función de la necesidad, generando ahorro de costes.
- *Hub* de integración en la nube, escalable en función de la demanda y sin necesidad de recursos de infraestructura por parte de los usuarios.
- De aplicación tanto a pymes como para grandes compañías.
- Solución escalable que permita incorporar progresivamente la conectividad con cada uno de los puertos a nivel nacional, y también ampliable a nivel internacional para operadores multinacionales, con un crecimiento progresivo del servicio.
- Pago en función del servicio y la necesidad especifica en cada momento.

Los beneficios que aporta solución propuesta desde la perspectiva de la innovación se pueden resumir en tres grandes áreas:

<!-- image -->

## 5 Impacto del proyecto y grado de implantación práctica

### 5.1 Impacto en el sector logístico-portuario

Los beneficiarios del proyecto TRANSLATE en el entorno logístico portuario son, por un lado, cualquier operador que pueda ser usuario de alguna plataforma digital de intercambio electrónico con los puertos y las administraciones, y por otro las Autoridades Portuarias y propietarios de plataformas digitales logísticas, que se podrán ver beneficiadas tanto por el incremento en el número de usuarios de sus plataformas como en la mejora en el uso de los servicios, al facilitar la integración con sus sistemas mediante mensajería electrónica.

La plataforma TRANSLATE va a cubrir una necesidad que actualmente se resuelve por cada uno de los actores (Autoridades Portuarias/PCS, Operadores Logísticos, Clientes, Proveedores,) de forma individual y punto a punto. Este modelo de solución supone, por cada uno de los agentes que requiere integrar sus sistemas con las plataformas logísticas de intercambio de información, disponer de equipamientos, sistemas y conocimientos técnicos y funcionales para su desarrollo, reservar recursos oportunos, técnicos y humanos para labores de mantenimientos, así como el desarrollo evolutivo de adaptaciones ante cualquier cambio normativo, legislativo o funcional que requiera una modificación.

TRANSLATE resuelve esta necesidad crítica de una forma diferente. TRANSLATE propone una solución centralizada que permite un crecimiento exponencial por el reaprovechamiento de los conectores, permite una reducción de costes de inversión y mantenimiento, minimiza errores y el consumo del servicio es a demanda.

Es importante destacar que la solución centralizada permitirá detectar y corregir de forma anticipada posibles cambios normativos, errores, caídas de servicio o incidencias. A modo de ejemplo, si un nodo, normalmente receptor o concentrador de mensajes (PCS de un puerto o Autoridad Portuaria) realiza algún ajuste o modificación en alguno de sus sistemas que requiere alguna adaptación de los mensajes a recibir, será suficiente con realizar los ajustes necesarios sobre el Hub de Integración Digital, evitando ajustes a realizar en todos los sistemas que conectan con ese receptor. Además, si la incidencia es sobrevenida, la plataforma detectará el problema en el primer envío pudiendo evitar errores posteriores.

Por todo lo mencionado, el potencial impacto y grado de implantación práctica de TRANSLATE a medio plazo es constituirse como la principal solución usada a nivel nacional como pasarela de interoperabilidad con la mayoría (si no todas) las plataformas de intercambio electrónico del sector portuario, evitando adaptaciones y desarrollo propios en cada uno de los sistemas particulares de las empresas, pasando a un consumo de servicio ajustado a la necesidad del intercambio de mensajes.

TRANSLATE ha conseguido atraer la atención e interés de la comunidad logística portuaria (empresas y operadores de transporte y autoridades portuarias) tal y como se observa en los compromisos de agente facilitador y cartas de apoyo recibidas por parte de distintos interesados. El motivo principal del gran interés generado por la plataforma TRANSLATE es debido a que se focaliza en una problemática todavía no resuelta que genera actualmente unos elevados consumos de recursos, cargas de gestión e impactos operativos a los diferentes operadores de la comunidad logística-portuaria.

### 5.2 Impacto en la sociedad y en la economía

El despliegue de una solución tecnológica como TRANSLATE para la optimización de servicios digitales de logística portuaria tiene un impacto relevante en el ámbito económico, social y medioambiental.

La digitalización de procesos está identificada como una de las principales palancas para impulsar la transformación del modelo económico y social. En la era de la revolución industrial 4.0, la transformación de los procesos aplicando las nuevas plataformas y tecnologías como cloud y blockchain, utilizadas en el desarrollo de TRANSLATE, tiene como resultado un aumento exponencial de la productividad.

La nueva economía 4.0 incluye nuevos modelos de negocio colaborativos, donde los operadores públicos y privados implantan procesos transversales y comunes, y comparten información mediante el uso de plataformas digitales. En el ámbito de la logística portuaria, estas plataformas incluyen los Port Community System, ventanillas únicas logísticas nacionales y europeas y plataformas digitales logísticas privadas. TRANSLATE contribuye a la implantación y el éxito de estas plataformas proporcionando servicios al alcance de cualquier operador logístico, con independencia de su tamaño, actividad y carácter público o privado.

Como conclusión, TRANSLATE impulsa el desarrollo económico y social de los entornos logístico-portuarios contribuyendo significativamente a la transformación digital de sus procesos y modelos de servicio.

### 5.3 Impacto en el medio ambiente

La introducción de la plataforma TRANSLATE tendrá un impacto positivo sobre el medio ambiente, al menos en dos aspectos:

- Hoy en día todavía hay muchos operadores que continúan utilizando el papel en sus procesos de intercambio de información. En este sentido, la digitalización de procesos que facilita TRANSLATE permitirá una reducción del consumo de papel en las empresas.
- La mejor y más eficiente gestión del transporte como resultado de una comunicación eficiente, completa, fiable y en el tiempo requerido entre los operadores del sector logístico portuario tiene como consecuencia la reducción del consumo energético y las emisiones contaminantes, cuantificable en la optimización del número de operaciones necesarias para la ejecución de un transporte.

## 6 Protección de la propiedad industrial

Una vez desarrollada la plataforma **TRANSLATE** y disponible en su nivel de madurez de TRL7 y en relación con los derechos de propiedad intelectual y uso de esta, planteamos la realización de las siguientes actuaciones:

- Para el uso de la Plataforma TRANSLATE, adicionalmente al contrato para hacer uso de los servicios, se incluirá un **Acuerdo de Confidencialidad** ( *NDA: Non-Disclosure Agreement* ) entre las partes, necesario también para cualquier acceso que se requiera a partes del código y de su arquitectura.
- Asimismo, en caso de no existir previamente términos de uso, se establecerán los correspondientes Acuerdos de uso y explotación con los diferentes proveedores que proporcionen librerías o componentes base para el software y que se encuentren integrados en la plataforma.
- Se integrarán en el desarrollo las medidas de seguridad necesarias, orientadas tanto a la protección del código fuente como a las buenas prácticas de desarrollo seguro y la debida confidencialidad de la información. En este sentido, el desarrollo y la gestión del proyecto estarán sujetos al cumplimiento de los procedimientos y controles especificados en el Sistema de Gestión de Seguridad de la Información (SGSI) de Infoport, certificado bajo la norma ISO 27001 y el Esquema Nacional de Seguridad (ENS).
- El contrato de uso y licencia de la plataforma TRANSLATE hará referencia a los Derechos de Propiedad Intelectual como desarrolladores completos de la solución y explotación posterior de la misma por parte de los socios del proyecto. Se solicitará el registro en el Registro de la Propiedad Intelectual (RPI)  en el epígrafe Software contenido en el capítulo de Programas de Ordenador.
- Se solicitará el registro de marca y logos de la Plataforma TRANSLATE para proteger la propiedad y su uso legítimo.

## 7 Justificación del nivel de madurez tecnológica inicial

### 7.1 Descripción general de la PoC

El proyecto de desarrollo de la plataforma **TRANSLATE** parte de una prueba de concepto inicial (PoC) con un nivel de madurez tecnológica y experimental **TRL5** (validación a nivel de componentes en un entorno relevante). Infoport ha desarrollado un sistema de integración para el envío y recepción de mensajería corporativa a distintas plataformas PCS, a partir de la experiencia adquirida en integración de sistemas con los distintos operadores económicos con los que trabaja.

Concretamente, hemos realizado una colaboración con el operador logístico internacional **TIBA Spain S.A.U.** y su filial en España, durante los años 2020 y 2021, con el objetivo de comprobar que la mensajería hacia los Port Comunity System de los puertos de Valencia ( **ValenciaportPCS)** y Barcelona ( **Portic)** se puede canalizar a través de una aplicación centralizada que permita que para la empresa sean transparentes los formatos específicos de los mensajes que esperan cada una de las plataformas de estas autoridades portuarias.

Esta prueba de concepto en fase temprana de la que partimos permite realizar el envío de determinados mensajes de TIBA hacia entornos de prueba de Valenciaportpcs, haciendo uso de varios modelos de integración. Cada uno de dichos modelos constituye una “traducción” de un mensaje concreto en el formato del operador a sus homólogos en las plataformas de mensajería. En el caso de Portic dado que no disponemos de un entorno de test como el de Valenciaportpcs verificamos la transformación de los mensajes en base a los mensajes originales proporcionados por TIBA.

Este proyecto ha sido, por tanto, una prueba de concepto del proyecto definitivo TRANSLATE, que cumplirá la misma función, pero ampliando el número de servicios con una integración de los sistemas de información reales y como plataforma PaaS multiempresa en la nube.

En esta fase, el despliegue se ha realizado sobre un servidor de Infoport donde se han instalado los componentes software necesarios.

Para poder realizar las pruebas de envío haciendo uso de la Api y el modelo de integración generado, se ha utilizado “Swagger”. Swagger no es más que una forma de poder ver las Web API en un interfaz Web en el navegador. Permite documentar la Web API ofrecida, indicando de qué manera se puede utilizar, permite describir el modelo de integración y además permite testear las Web APIi.

La prueba de concepto incluye los siguientes módulos funcionales:

- **Una web API** desarrollada con tecnología .Net 5 donde se publica un método web que ofrece el modelo de integración y que la plataforma se encarga de transformar para realizar los envíos de los mensajes en el formato esperado por ValenciaportPcs o Portic.
- Un back-end en el que internamente se implementan las **transformaciones de los modelos de integración** en los mensajes esperados por las plataformas y realiza el envío hacia las mismas con las credenciales de los entornos de test correspondientes. Se encarga del almacenamiento en disco de los mensajes y de su registro en base de datos.
- Esquemas y motores de **bases de datos relacionales** (MariaDB).

El esquema de arquitectura de alto nivel de la prueba de concepto realizada se representa en el siguiente diagrama:

<!-- image -->

### 7.2 Sistema de integración con Valenciaportpcs y Portic

La PoC inicial para determinar la viabilidad de la plataforma y su sentido, pasó por decidir en primer lugar qué servicio existente era susceptible de ser integrado por TRANSLATE en tanto en Valenciaportpcs como en Portic. El servicio seleccionado fue el de Transporte Terrestre .

Dentro de este servicio, en ambos PCS se ofrecen para la recepción de órdenes de transporte terrestre de importación y exportación distintos estándares de mensajería. En el caso de Valenciaportpcs es el Documento Único de Transporte (DUT) y en el caso de Portic el IFTMIN2I05 y el IFTMINE03. Mediante estos documentos un consignatario u operador logístico puede enviar órdenes de trasporte terrestre al puerto de Valencia y Barcelona.

La idea consiste en que, a partir de toda la información requerida por ambos PCS para una orden de transporte terrestre, se genere un único modelo de integración dentro de la plataforma TRANSLATE que permita el envío de órdenes de transporte terrestre a ambos puertos. Este modelo debe incluir todas las necesidades de información de forma conjunta y unificada. El modelo de integración creado es el mensaje **IntegrationOrder** . A continuación, se detallan los mensajes de los PCS incluidos en la PoC y la definición del mensaje genérico para transporte terrestre IntegrationOrder.

#### 7.2.1 Documento Único de Transporte (DUTv2) de Valenciaportpcs

El mensaje de Documento Único de Transporte (DUTv2) se enmarca en el conjunto de mensajes modelados por Valenciaportpcs para la ordenación del transporte terrestre entre demandantes de transporte, proveedores de transporte, proveedores del equipamiento (contenedor) y empresas de entrega y admisión del equipamiento.

El mensaje de Documento Único de Transporte se utiliza para que el demandante de transporte pueda trasladar al proveedor de este (identificado en el modelo de valenciaportpcs.net como el operador de transporte) las instrucciones para realizar un transporte por carretera de uno o varios equipamientos (hasta el momento, limitado a contenedores). En el mismo documento, además de las instrucciones de transporte pueden venir incorporadas las órdenes de entrega y admisión de cada contenedor. Si el emisor del documento es a su vez el proveedor del equipamiento y tiene, por tanto, potestad para emitir dichas órdenes a las empresas encargadas de la entrega y admisión, éstas pueden incluirse directamente en el documento único emitido.

#### 7.2.2 Mensajes IFTMIN2I05 y IFTMINE03 de Portic

El mensaje IFTMIN2I05 (Importación) se utiliza para comunicar, por parte de la entidad responsable de la organización del transporte terrestre (Agente de Aduanas, Transitario o Consignatario) a la empresa de transportes o transportista autónomo, todos los detalles asociados a la recogida de contenedores o mercancías en la Terminal y su entrega al importador. La responsabilidad de la organización del transporte terrestre puede corresponder a diferentes entidades: Consignatario, Transitario o Agente de Aduanas. El emisor del mensaje IFTMIN2 comunica al transportista todos los detalles sobre la recogida de la mercancía, la entrega de la carga al importador y la devolución del equipamiento vacío una vez completado el proceso de entrega.

El IFTMINE03 (exportación) se utiliza para comunicar, por parte de la entidad responsable de la organización del transporte (Agente de Aduanas, Transitario o Consignatario) a la empresa de transportes o transportista autónomo, todos los detalles asociados a la recogida de contenedores vacíos en el Depósito o Terminal, a la recogida de la mercancía en el expedidor y a su posterior entrega en la Terminal.

#### 7.2.3 Modelo de integración IntegrationOrder

El modelo de integración **IntegrationOrder** incluye toda la información relativa a una orden de transporte terrestre, en un formato que presenta una semántica completa, genérica e independiente de las plataformas destino para las que se va a transformar.

En el siguiente esquema se muestra una visión global de la estructura ofrecida por el modelo IntegrationOrder:

<!-- image -->

<!-- image -->

### 7.3 Esquema detallado de la PoC

#### 7.3.1 Funcionamiento detallado

Para la prueba de concepto se han desarrollado y validado los módulos de la plataforma TRANSLATE necesarios para los siguientes mensajes y procesos:

- **Mensajes:**
    - TIBA proporciona una batería de mensajes XML DUT, IFTMIN2I05 y IFTMINE03. Estos mensajes proceden de los sistemas de TIBA. Los mensajes se obtienen a partir de mensajes reales utilizados por TIBA en su operativa.
    - Como el proceso de envío requiere modelos IntegrationOrder se realiza un proceso de transformación de los mensajes proporcionados por TIBA para la realización de las pruebas en el entorno de test. El resultado es un conjunto de mensajes JSON IntegrationOrder de prueba.
- **Procesos:**
    - A partir de los mensajes JSON de prueba IntegrationOrder se realiza el envío en TRANSLATE mediante el interfaz web ofrecido para la Web API. Una vez la Web API recibe el modelo de integración, este se almacena en disco y se registran los metadatos de control en una base de datos ***MariaDB*** junto con la auditoria de recepción del mismo.
    - El módulo de conversión de la plataforma realiza las correspondientes traducciones de los mensajes al formato utilizado por cada destinatario, en el caso que nos ocupa, para Valenciaportpcs y Portic. El propio mensaje indica el destinatario del mismo para que TRANSLATE se ocupe de la traducción de forma automática.
    - Envío de los mensajes. Los mensajes se envían mediante llamada a servicio web a Valenciaportpcs en formato XML o a la plataforma Portic.

#### 7.3.2 API ofrecido en la prueba de concepto

En la prueba, TRANSLATE ofrece un API con un método web llamado IntegrationOrder.

Como ya hemos comentado se ha utilizado una tecnología (Swagger) ampliamente usada y considerada casi un estándar de facto en el diseño de las Web API. Se puede observar en la siguiente imagen cómo se proporciona un interfaz de la Web API dl PoC. En la propia interfaz aparece documentado el modelo IntegrationOrder y además ofrece la funcionalidad de testing sobre la misma.

<!-- image -->

Se puede observar cómo queda documentado el modelo IntegrationOrder:

<!-- image -->

#### 7.3.3 Resultados de la prueba de concepto

##### 7.3.3.1 Mensajes utilizados y transformaciones realizadas

Para la realización de las pruebas, tal y conforme se ha descrito previamente, se han utilizado mensajes proporcionados por TIBA en su operativa con Valenciaport y con Portic. Estos han sido transformados a IntegrationOrder, que es el modelo de integración esperado por TRANSLATE en la PoC propuesta. En las siguientes carpetas se muestra la jerarquía de dichos mensajes.

<!-- image -->

<!-- image -->

<!-- image -->

##### 7.3.3.2 Verificaciones realizadas en las pruebas

Con cada prueba realizada de envío de un IntegrationOrder hemos verificado:

- Que se almacena en el *filesystem* de TRANSLATE el mensaje original y el transformado. Se verifica que la transformación coincida con la original proporcionada por TIBA.
- Que se almacenan en la base de datos los datos del mensaje recibido y los datos de control del mensaje. En el envío, los datos de control del mensaje se reducen a su MessageNumber ya que todavía no se dispone de información de respuesta del PCS.
<!-- image -->
<!-- image -->
- Se accede al entorno de test, en el caso de Valenciaportpcs, para verificar que se ha recibido la orden de transporte. En el caso de Portic se verifican solamente las transformaciones de los mensajes.

## 8 Plan para la realización del prototipo en entorno real

### 8.1 Descripción del demostrador de la plataforma TRANSLATE

El demostrador de la plataforma **TRANSLATE** que la llevará a **TRL7** consistirá en una plataforma de mensajería en la nube (basada en tecnología Docker) que deberá exponer, para las empresas usuarias asociadas, una serie de API de integración de mensajería con distintas autoridades portuarias o plataformas electrónicas, para el envío y recepción de distintos tipos de mensajes necesarios para la operativa portuaria. La empresa asociada hará uso de modelos de integración únicos que se transformarán en los distintos mensajes esperados según la configuración de los destinatarios de dichos mensajes.

Para ello TRANSLATE ofrecerá un conjunto de modelos de integración mediante API en formato JSON que unificarán la información requerida para los distintos servicios portuarios (terrestre, escalas, aduana, etc.) de las distintas autoridades portuarias u otros modelos de integración con otras plataformas electrónicas. Esto le permite a la empresa asociada desentenderse del formato específico esperado por cada Autoridad Portuaria o plataforma ya que TRANSLATE se encargará de las transformaciones necesarias y además podrá trazar toda la mensajería de la empresa enviada y recibida garantizando su auditoría.

Uno de los puntos más relevantes de TRANSLATE será el componente **Translate Adapter** que va a permitir, para empresas con problemas de integración con cualquier tipo de servicio web, facilitarles la interoperabilidad a través de TRANSLATE y, por ende, con todas las integraciones que ofrece TRANSLATE.

Estas empresas suelen tener problemas relacionados con la incapacidad técnica, o con limitaciones fuertes a nivel de seguridad en la salida o entrada de información, o disponen de sistemas cerrados que impiden este tipo de conexiones o simplemente porque no son capaces de generar los mensajes esperados por los PCS u otras plataformas electrónicas y necesitan una transformación inicial desde sus formatos. En muchos casos solo pueden generar salidas de información del tipo ficheros en carpetas, completar una Excel, mandar correos electrónicos, etc. Translate Adapter se encargará de hacer uso de estas capacidades de la empresa que se desea integrar y conectarles con el sistema TRANSLATE. Además, si requieren de una transformación de su información a los modelos de integración ofrecidos por TRANSLATE, Translate Adapter se encarga de realizar también estas adaptaciones.

Una vez realizado el envío a TRANSLATE de los modelos de integración por parte de la empresa, bien por sus propios medios o haciendo uso de Translate Adapter, la empresa podrá consultar la trazabilidad de estos mensajes desde un **Interfaz Web para Clientes** que le permita revisar todo el log de envíos y recepciones.

Este es el esquema general de la plataforma:

<!-- image -->

#### 8.1.1 Proceso de envío de un modelo de integración

El proceso que seguirá internamente TRANSLATE ante la recepción de un modelo de integración consiste en lo siguiente:

- En primer lugar, verificar que la empresa, con las credenciales que se la han facilitado para su integración puede mandar este modelo de integración.
- Si la entrada es correcta, se almacena el modelo original recibido en el **Cloud Storage**
- Se registra en base de datos los datos básicos del modelo mediante el componente **Repository** , para que desde la Interfaz Web para Clientes este disponible esta información.
- Se inserta en el **Message Broker** en una cola específica para la empresa remitente del modelo de integración y tipo de modelo recibido.
- Se integra el modelo recibido en **Blockchain** garantizando la invariabilidad del mismo.
- La lógica de negocio se encarga de consultar todas las colas de mensajería pendientes de procesar y realiza las siguientes acciones para cada modelo de integración:
    - En primer lugar, determina para dicha empresa y modelo de integración qué destinatarios tiene configurados y a qué formatos de mensaje se debe realizar la transformación.
    - Para cada destinatario configurado:
        - Se realiza el proceso de transformación del mensaje.
        - Se almacena el mensaje transformado en el Cloud Storage.
        - Se almacena en base de datos el log de la transformación realizada.
        - Se inserta en el broker de mensajería el mensaje transformado en una cola específica para la empresa remitente, destinatario y tipo de mensaje de salida.
- El componente **Message Integration** se encarga de procesar todos los mensajes pendientes de enviar a partir de las colas de salida y para cada mensaje:
    - Obtiene la configuración de seguridad de acceso para el destinatario para poder invocar al servicio configurado en el envío.
    - Se realiza el envío al PCS o plataforma destinataria.

**La aportación que puede tener Translate Adapter sobre el proceso de envío** a modo de ejemplo podría ser la recepción de mensajes por parte del cliente como adjuntos por correo electrónico pudiendo configurar las credenciales de acceso al correo, convertir dicho adjunto en un modelo de integración y enviarlo a TRANSLATE. O configurar el acceso a una cuenta Google Drive para compartir carpetas entre el sistema del cliente y Translate Adapter y mediante las credenciales de Google Drive acceder a la información del cliente, generar los modelos de integración y enviarlos a TRANSLATE. Incluso sería posible la recepción por ftp. Las transformaciones específicas para clientes se incluyen en este componente.

#### 8.1.2 Proceso de recepción de un modelo de integración

Para la recepción de mensajes desde PCS o plataforma electrónica el proceso es el siguiente:

- El cliente tendrá configuradas las plataformas de ls cuales espera mensajes. Tendrá configurada la seguridad de acceso a las mismas en TRANSLATE y el componente Message Integration se encarga de acceder a las mismas y descargar los mensajes.
- Para cada mensaje descargado:
    - Se almacena el modelo original recibido en el **Cloud Storage**
    - Se registra en base de datos los datos básicos del mensaje mediante el componente **Repository** , para que desde la Interfaz Web para Clientes este disponible esta información.
    - Se inserta en el **Broker de Mensajería** en una cola específica para la plataforma remitente, empresa cliente y tipo de mensaje recibido.
    - Se integra el mensaje recibido en **Blockchain** garantizando la invariabilidad del mismo.
- La lógica de negocio se encarga de consultar todas las colas de mensajería de mensajes descargados y realiza las siguientes acciones para cada mensaje:
    - En primer lugar, determina para la empresa cliente, plataforma de origen y tipo de mensaje que receptores tiene configurados y a que formatos de mensaje se debe realizar la transformación. Puede que no sea solo la propia empresa cliente la que reciba el modelo de integración, podría configurar otras empresas de TRANSLATE que también lo necesiten recibir.
    - Para cada receptor configurado:
        - Se realiza el proceso de transformación del mensaje.
        - Se almacena el mensaje transformado en el Cloud Storage.
        - Se almacena en base de datos el log de la transformación realizada.
        - Se inserta en el broker de mensajería el mensaje transformado en una cola específica para la plataforma remitente, empresa destinataria y tipo de modelo de integración de salida.
- A partir de este punto las empresas receptoras podrían acceder al servicio web de salida del modelo de integración esperado y descargar los mensajes. Con cada descarga se realiza una inserción en el log de la BBDD.

**La aportación que puede tener Translate Adapter sobre el proceso de recepción** sería similar a los mismos casos expuestos en el envío, pero en este caso en la descarga, realizando una transformación previa del modelo de integración descargado y depositando el mensaje resultante como lo requiera el cliente según su necesidad y limitaciones en cualquiera de las formas que admita Translate Adapter. Las transformaciones específicas para clientes se incluyen en este componente.

### 8.2 Caso de uso 1: Integración de MSC Consignataria

El proceso de envío y de recepción de mensajes de este caso de uso es el que definido en el punto 8.1

Para el prototipo del agente facilitador MSC será necesario configurar Translate Adapter de la siguiente manera:

- En el envío
    - Convertir el formato del Vermas de MSC en IntegrationVermas
    - Convertir los mensajes DUT/RO/AO en formato IntegrationOrder.
    - Convertir las listas de carga COPRAR en IntegrationList
- Para la recepción de mensajes
    - Se debe convertir el IntegrationVermas en el formato Vermas de MSC.

El esquema del demostrador para la integración de le empresa facilitadora MSC con rol consignatario es el siguiente:

<!-- image -->

### 8.3 Caso de uso 2: Integración de PCS de APV – TRADELENS

En el caso del prototipo de APV, en este momento ya se generan desde el PCS algunos mensajes relacionados con eventos para TRADELENS. La idea es hacer pasar estos mensajes por TRANSLATE a modo de auditoría del mensaje enviado. En este caso no se define un modelo de integración, el mismo mensaje de TRADELENS se toma como modelo de integración. Esto es posible en TRANSLATE cuando el modelo de integración es el mismo que el mensaje de destino.

En este caso, solo estamos auditando mediante TRANSLATE el envío de eventos a TRADELENS por parte de APV. El hacerlo de esta manera daría la posibilidad a APV a futuro que si el mismo tipo de eventos enviados a TRADELENS como “una salida por puertas”, otra plataforma los requiere con tan solo realizar la transformación en TRANSLATE y configurar los dos destinatarios ya lo tendría resuelto sin desarrollo alguno.

De la misma manera APV, podría ofrecer servicios de integración a otras plataformas electrónicas u otros PCS que pasando por APV y TRANSLATE, permitiesen su transformación y envío a destinatarios, incluso con la posibilidad de hacer uso de Translate Adapter si tienen algún tipo de limitación técnica.

El esquema del demostrador para la integración de le empresa facilitadora APV es el siguiente:

<!-- image -->

### 8.4 Componentes de la nueva plataforma PaaS TRANSLATE

#### 8.4.1 Identity Manager

El Identity Manager garantiza que solamente las personas autorizadas, y nadie más, tengan acceso a los recursos tecnológicos que necesitan para realizar su trabajo. Incluye las políticas y tecnologías que conforman un proceso, que abarca toda la organización, para identificar, autenticar y autorizar adecuadamente a personas, grupos de personas o aplicaciones de software a través de atributos como los derechos de acceso de los usuarios y las restricciones basadas en sus identidades.

En TRANSLATE desde el gestor de identidades se dan de alta las empresas integradas con una credencial de acceso que permite a identificar la empresa cliente que ha accedido al interfaz web para clientes o al interfaz web de administración o incluso que empresa está haciendo uso de las APIs de integración.

#### 8.4.2 APIs de Envío y Recepción de Modelos de Integración

##### 8.4.2.1 APIs expuestas

Las API que se exponen en TRANSLATE son cada uno de los servicios web necesarios para el envío o la recepción de modelos de integración. Estas están securizadas mediante credencial de acceso con el Identity Manager.

##### 8.4.2.2 Logic/Transformations

La lógica del Core de la aplicación es la que se encarga de enlazar todos los componentes en el proceso de envío y recepción de modelos de integración, estableciendo un flujo de traspaso de información entre cada componente coherente y realizando las validaciones pertinentes en cada proceso.

Las transformaciones son cada una de las conversiones realizadas entre modelos de integración o mensajes tanto en un sentido como en otro.

##### 8.4.2.3 Repository

El repositorio se encarga de acceder a la base de datos para la consulta o creación de información.

##### 8.4.2.4 Message Integration

El componente de integración de mensajes hace uso de la configuración de seguridad de acceso establecida por cada cliente, para acceder a la empresa destinataria u originadora de mensajes, bien sea un PCS o una plataforma electrónica, para el envío y la recepción de mensajes.

#### 8.4.3 Translate Adapter

Translate Adapter permite que empresas con problemas de integración con cualquier tipo de servicio web, facilitarles el proceso de integración con TRANSLATE y, por ende, con todas las integraciones que ofrece TRANSLATE.

Estas empresas suelen tener problemas relacionados con la incapacidad técnica, o con limitaciones fuertes a nivel de seguridad en la salida o entrada de información, o disponen de sistemas cerrados que impiden este tipo de conexiones o simplemente porque no son capaces de generar los mensajes esperados por los PCS u otras plataformas electrónicas y necesitan una transformación inicial desde sus formatos. En muchos casos solo pueden generar salidas de información del tipo ficheros en carpetas, completar una Excel, mandar correos electrónicos, etc. Translate Adapter se encargará de hacer uso de estas capacidades de la empresa que se desea integrar y conectarles con el sistema TRANSLATE. Además, si requieren de una transformación de su información a los modelos de integración ofrecidos por TRANSLATE, Translate Adapter se encarga de realizar también estas adaptaciones.

Esto permite que una empresa que pueda depositar ficheros en Google Drive, One Drive, etc. o enviar correos con mensajes adjuntos o pueda hacer envíos mediante ftp entre otras posibilidades que se manejan para el adaptador puedan integrarse con TRANSLATE.

#### 8.4.4 Message Broker

El bróker de mensajería se encarga de encolar todas las listas de mensajes enviados/recibidos pendientes de transformar, todos los mensajes transformados pendientes de enviar/recibir. Todo ello garantizando la persistencia de las colas de mensajería en caso de fallo o caídas del sistema.

#### 8.4.5 Database

La base de datos se utiliza para gestionar los datos de control de los mensajes enviados y recibidos, la auditoria de los mismos, la configuración de las empresas integradas, etc.

#### 8.4.6 Cloud Storage

Los mensajes transformados a JSON o XML se almacenan en un almacenamiento en la nube de forma que puedan ser accesibles desde el Interfaz Web del Cliente.

#### 8.4.7 Blockchain

Blockchain se puede definir como una estructura matemática para almacenar datos de una manera que es casi imposible de falsificar. Es un libro electrónico público que se puede compartir abiertamente entre usuarios dispares y que crea un registro inmutable de sus transacciones. En este punto los mensajes se almacenan en Blockchain, garantizando que el mensaje original no ha sido variado por la plataforma y su transformación tampoco.

#### 8.4.8 Client Site

La web del cliente permite ver la auditoría de mensajes enviados y recibidos. A su vez podrá ver la configuración establecida para su empresa en cuanto a sus integraciones, configuración de seguridad con las distintas plataformas, etc.

#### 8.4.9 Admin Site

La web de administración básicamente se usa para el alta de nuevas empresas, especificación de transformaciones, destinatarios de estas transformaciones, etc. Consiste en el componente que permite configurar TRANSLATE como PaaS.

### 8.5 Plan de trabajo para el desarrollo de la plataforma y el demostrador

A continuación, se detalla el plan previsto para la realización y presentación de la plataforma **TRANSLATE** y sus dos casos de uso, con las tareas requeridas y comprometidas por los agentes facilitadores.

La duración completa del plan previsto para el desarrollo de la plataforma es de 24 meses y contempla dos fases:

- **Fase 1: Desarrollo de la plataforma PaaS** . Consiste en la configuración y despliegue de todos los elementos necesarios para la realización del prototipo en entorno real, que previamente han sido testeados en entorno de test. Esta fase corresponde principalmente al equipo de **Infoport** asignado al proyecto **TRANSLATE** (detallado en el capítulo siguiente, capítulo 9) con la colaboración de una empresa subcontratada para la parte de la integración con Blockchain.

- **Fase 2: Desarrollo de los demostradores de MSC y APV.** Consiste en trasladar las funcionalidades de mensajería conforme se describen en los apartados 8.2 y 8.3, realizar todo el testeo y pruebas previas para el arranque en productivo. Durante toda esta fase dispondremos de los recursos necesarios por parte de **MSC y APV** para el seguimiento, aprobación y puesta en producción del prototipo. Para ello, MSC y APV conectarán sus sistemas de información de pruebas a TRANSLATE, manteniendo en funcionamiento el piloto al menos hasta que se produzca el lanzamiento al mercado de la plataforma.

El resumen de hitos y fases se muestra en la siguiente tabla:

| Hito   | Nombre del Hito                                            | Fase relacionada   | Mes fin   |
|--------|------------------------------------------------------------|--------------------|-----------|
| H1     | Disponibilidad de la plataforma base de TRANSLATE en cloud | Fase 1             | M16       |
| H2     | Disponibilidad del demostrador del caso de uso 1           | Fase 2             | M24       |
| H3     | Disponibilidad del demostrador del caso de uso 2           | Fase 2             | M24       |

Se muestra a continuación la relación de actividades (paquetes de trabajo) del proyecto, con su calendario aproximado de ejecución y dedicación estimada en horas totales:

| Paquete de trabajo   | Nombre del paquete de trabajo                       | Horas totales   | Hito   | Mes inicio   | Mes fin   |
|----------------------|-----------------------------------------------------|-----------------|--------|--------------|-----------|
| PT1                  | Investigación y análisis de la solución en la nube. | 339             | H1     | M1           | M3        |
| PT2                  | Análisis funcional de la plataforma                 | 348             | H1     | M2           | M4        |
| PT3                  | Diseño y construcción de la solución en la nube     | 2.808           | H1     | M5           | M16       |
| PT4                  | Análisis del caso de uso 1                          | 313*            | H2     | M13          | M15       |
| PT5                  | Desarrollo e implementación del caso de uso 1       | 1.187           | H2     | M14          | M24       |
| PT6                  | Análisis del caso de uso 2                          | 184**           | H3     | M19          | M21       |
| PT7                  | Desarrollo e implementación del caso de uso 2       | 401             | H3     | M21          | M24       |

* Se incluyen 60 horas a realizar por el Agente Facilitador 1 (MSC)

** Se incluyen 20 horas a realizar por el Agente Facilitador 2 (APV)

#### 8.5.1 PT1: Investigación y análisis de la solución en la nube

##### 8.5.1.1 Objetivos

Investigar y analizar todos los componentes que van a formar parte de la solución final, para poder disponer de una plataforma como servicio en la nube (PaaS).

##### 8.5.1.2 Descripción del trabajo a realizar

Se va a realizar un análisis de cada componente identificado en el punto 8.4, en algún caso como la integración de Blockchain va a requerir de una formación el equipo y de apoyo de una empresa experta en modo subcontratación. En este punto, se decidirá las tecnologías a utilizar de cada componente y como se hará el despliegue final.

Por otra parte, también se hará un análisis de datos open data estadísticos de las transacciones.

Al final de este paquete se tendrá un documento de análisis y despliegue de la solución en la nube.

| Tarea   | Descripción                                                            |   Horas estimadas | Perfiles requeridos    |
|---------|------------------------------------------------------------------------|-------------------|------------------------|
| T1.1    | Control y seguimiento                                                  |                30 | Director de proyecto   |
| T1.2    | Análisis del alojamiento de la plataforma                              |                40 | Arquitecto             |
| T1.3    | Análisis sobre que Identity Manager usar                               |                30 | Arquitecto             |
| T1.4    | Análisis sobre qué base de datos usar                                  |                30 | Arquitecto             |
| T1.5    | Formación en Blockchain                                                |               120 | Arquitecto             |
| T1.6    | Investigación sobre integración con Blockchain                         |                40 | Arquitecto             |
| T1.7    | Análisis y diseño de datos open data estadísticos de las transacciones |                40 | Arquitecto             |
| T1.8    | Validar requisitos técnicos                                            |                 9 | Director de tecnología |

##### 8.5.1.3 Resultados y entregables

| Entregable   | Nombre del entregable                                        | Tipo entregable   | Nivel de diseminación   | Mes entrega   |
|--------------|--------------------------------------------------------------|-------------------|-------------------------|---------------|
| E1.1         | Documento de análisis y despliegue de la solución en la nube | Documento         | Privado                 | M3            |

#### 8.5.2 PT2: Análisis funcional de la plataforma

##### 8.5.2.1 Objetivos

Disponer de un análisis de la Web de Administración para poder configurar las distintas plataformas, las empresas y delegaciones, y el modo de conexión entre los clientes y la plataforma. También, disponer de un análisis de la Web de Cliente, disponible para los clientes para que puedan hacer seguimiento de toda la auditoría de mensajes enviados y recibidos.

##### 8.5.2.2 Descripción del trabajo a realizar

Primero se hará el análisis funcional del diseño de la base de datos para las Web de Administración y de Cliente, luego se analizará las diferentes formas de integración de mensajes dentro de la plataforma (API rest, FTP, correo electrónico, Google Drive…) que se utilizarán en Translate Adapter.

Por último, se hará el análisis de la Web de Administración y de la Web de Cliente, donde se definirán las historias necesarias.

De este paquete saldrán 4 entregables, que serán documentos de análisis del diseño de la base de datos, de la integración de mensajes, de la Web de Administración y de la Web Cliente.

| Tarea   | Descripción                                 |   Horas estimadas | Perfiles requeridos    |
|---------|---------------------------------------------|-------------------|------------------------|
| T2.1    | Control y seguimiento                       |                30 | Director de proyecto   |
| T2.2    | Análisis del diseño de la base de datos     |                40 | Analista               |
| T2.3    | Análisis de la integración de mensajes      |                80 | Analista               |
| T2.4    | Análisis funcional de la Web Administración |                80 | Analista               |
| T2.5    | Análisis funcional de la Web cliente        |               100 | Analista               |
| T2.6    | Validar requisitos de negocio               |                 9 | Director de negocio    |
| T2.7    | Validar requisitos técnicos                 |                 9 | Director de tecnología |

##### 8.5.2.3 Resultados y entregables

| Entregable   | Nombre del entregable                                    | Tipo entregable   | Nivel de diseminación   | Mes entrega   |
|--------------|----------------------------------------------------------|-------------------|-------------------------|---------------|
| E2.1         | Documento del diseño de la base de datos                 | Documento         | Privado                 | M4            |
| E2.2         | Documento de análisis de la integración de mensajes      | Documento         | Privado                 | M4            |
| E2.3         | Documento de análisis funcional de la Web Administración | Documento         | Privado                 | M4            |
| E2.4         | Documento de análisis funcional de la Web cliente        | Documento         | Privado                 | M4            |

#### 8.5.3 PT3: Diseño y construcción de la solución en la nube.

##### 8.5.3.1 Objetivos

Disponer de la plataforma como en la nube (PaaS) que unificará diferentes componentes de mensajería. Esta plataforma será multiempresa, se podrán configurar múltiples empresas y delegaciones.

Asimismo, existirán dos aplicaciones web, una para la parte de administración y otra para los clientes, donde podrán visualizar la auditoría de sus mensajes enviados y recibidos.

##### 8.5.3.2 Descripción del trabajo a realizar

Basándonos en el entregable E1.1 del PT1, nos dispondremos a implementar cada uno de los componentes que tiene la plataforma en la tecnología elegida.

Para el desarrollo de este paquete hay tres partes diferenciadas una que será todo lo relacionado con la plataforma y la implementación de todos sus componentes, y otras dos que serán la parte visual de la plataforma web de administración y la de cliente.

En lo relacionado con la tarea T3.4 necesitaremos del apoyo de la empresa subcontratada, para poder hacer la implementación de la integración con Blockchain.

En este paquete dispondremos de cuatro entregables: los datos open data estadísticos de las transacciones, que serán públicos, de la plataforma en la nube, de la Web de Administración y de la Web de Cliente.

| Tarea   | Descripción                                                         |   Horas estimadas | Perfiles requeridos              |
|---------|---------------------------------------------------------------------|-------------------|----------------------------------|
| T3.1    | Control y seguimiento                                               |               240 | Director de proyecto             |
| T3.2    | Implementación del Identity Manager                                 |                40 | Arquitecto                       |
| T3.3    | Creación de la base de datos                                        |                40 | Desarrollador back               |
| T3.4    | Implementación de la integración con Blockchain                     |               160 | Arquitecto 160h, Subcontratación |
| T3.5    | Configurar el broker de mensajería                                  |                80 | Arquitecto                       |
| T3.6    | Configurar el cloud storage                                         |                40 | Arquitecto                       |
| T3.7    | Implementación del Message Integration                              |               160 | Desarrollador back               |
| T3.8    | Implementación de la lógica de negocio                              |               320 | Desarrollador back               |
| T3.9    | Implementación de Translate Adapter                                 |               160 | Desarrollador back               |
| T3.10   | Implementación de datos open data estadísticos de las transacciones |               100 | Desarrollador back               |
| T3.11   | Despliegue de los distintos dockers en la nube                      |                40 | Release Manager                  |
| T3.12   | Testeo de la plataforma                                             |                40 | Tester                           |
| T3.13   | Desarrollo front de la Web Administración                           |               320 | Desarrollador front              |
| T3.14   | Desarrollo back de la Web Administración                            |               200 | Desarrollador back               |
| T3.15   | Despliegue de la Web Administración                                 |                26 | Release Manager                  |
| T3.16   | Testeo de la Web Administración                                     |                52 | Tester                           |
| T3.17   | Desarrollo front de la Web Cliente                                  |               360 | Desarrollador front              |
| T3.18   | Desarrollo back de la Web Cliente                                   |               240 | Desarrollador back               |
| T3.19   | Despliegue de la Web Cliente                                        |                30 | Release Manager                  |
| T3.20   | Testeo de la Web Cliente                                            |                60 | Tester                           |
| T3.21   | Validar requisitos de negocio                                       |                50 | Director de negocio              |
| T3.22   | Validar requisitos técnicos                                         |                50 | Director de tecnología           |

##### 8.5.3.3 Resultados y entregables

| Entregable   | Nombre del entregable                       | Tipo entregable   | Nivel de diseminación   | Mes entrega   |
|--------------|---------------------------------------------|-------------------|-------------------------|---------------|
| E3.1         | Open data estadísticos de las transacciones | Software          | Público                 | M9            |
| E3.2         | Despliegue de la plataforma                 | Software          | Privado                 | M12           |
| E3.3         | Web Administración                          | Web               | Privado                 | M12           |
| E3.4         | Web cliente                                 | Web               | Privado                 | M16           |

#### 8.5.4 PT4: Análisis del caso de uso 1

##### 8.5.4.1 Objetivos

Analizar y definir la mensajería a implementar para el agente facilitador 1 (MSC), en las plataformas de PCS Valenciaportpcs y Portic.

##### 8.5.4.2 Descripción del trabajo a realizar

Se hará un análisis de los mensajes de Transporte Terrestre, Vermas y de las Listas de Carga/Descarga del agente facilitador 1. Y se estudiará de qué manera el agente facilitador puede enviar o recibir esta información. Según las posibilidades del cliente, se analizará como será el uso de Translate Adapter para que se pueda realizar los intercambios de mensajes en las distintas plataformas.

El entregable de este paquete será disponer de un documento de análisis para el caso de uso 1 del agente facilitador 1.

| Tarea   | Descripción                                              |   Horas estimadas | Perfiles requeridos                    |
|---------|----------------------------------------------------------|-------------------|----------------------------------------|
| T4.1    | Control y seguimiento                                    |                20 | Director de proyecto                   |
| T4.2    | Análisis de la mensajería Transporte Terrestre           |                67 | Analista 47h, Agente Facilitador 1 20h |
| T4.3    | Análisis de la mensajería Vermas (Peso Bruto Verificado) |                67 | Analista 47h, Agente Facilitador 1 20h |
| T4.4    | Análisis de la mensajería Listas de Carga/Descarga       |                67 | Analista 47h, Agente Facilitador 1 20h |
| T4.5    | Análisis de la integración con Translate                 |                40 | Analista                               |
| T4.6    | Análisis de la configuración en Translate                |                40 | Analista                               |
| T4.7    | Validar requisitos de negocio                            |                 6 | Director de negocio                    |
| T4.8    | Validar requisitos técnicos                              |                 6 | Director de tecnología                 |

##### 8.5.4.3 Resultados y entregables

| Entregable   | Nombre del entregable                   | Tipo entregable   | Nivel de diseminación   | Mes entrega   |
|--------------|-----------------------------------------|-------------------|-------------------------|---------------|
| E4.1         | Documento de análisis del caso de uso 1 | Documento         | Privado                 | M15           |

#### 8.5.5 PT5: Desarrollo e implementación del caso de uso 1

##### 8.5.5.1 Objetivos

Disponer de un hub de integración digital (HID), con la integración de ciertos mensajes con el PCS de APV (ValenciaPortPCS) y el PCS de APB (PORTIC). El diseño de la plataforma permitirá la interoperabilidad con estos dos PCS con lo que se demostrará que la solución será multiplaforma.

##### 8.5.5.2 Descripción del trabajo a realizar

Lo primero será configurar a la empresa del agente facilitador 1 indicando las plataformas y los mensajes que quiere enviar y recibir.

Siguiendo el documento de análisis del PT4, iremos implementando los distintos mensajes, para la plataforma de APV será Transporte Terrestre, el Vermas y las Listas de Carga/Descarga. Y para la plataforma de APB será Transporte Terrestre y Listas de Carga/Descarga.

Dependiendo de las posibilidades de integración del agente facilitador, tendremos que hacer un mapeo de sus datos a la plataforma Translate utilizando Translate Adapter.

Las plataformas de APV y APB permiten poder hacer pruebas de integración en un entorno de Test, que será el que utilizaremos para comprobar el funcionamiento de la plataforma.

El agente facilitador 1 tiene que participar en este paquete para poder testear que efectivamente los mensajes de envío y recepción son correctos en las distintas plataformas.

Una vez puesto en marcha el demostrador, se realizará el mantenimiento operativo del piloto durante el periodo requerido.

| Tarea   | Descripción                                               |   Horas estimadas | Perfiles requeridos    |
|---------|-----------------------------------------------------------|-------------------|------------------------|
| T5.1    | Control y seguimiento                                     |                90 | Director de proyecto   |
| T5.2    | Configuración de la empresa en la plataforma              |                20 | Arquitecto             |
| T5.3    | Implementación de la mensajería Transporte Terrestre      |               320 | Desarrollador back     |
| T5.4    | Implementación de Translate Adapter Transporte Terrestre  |                40 | Desarrollador back     |
| T5.5    | Despliegue de la mensajería Transporte Terrestre          |                18 | Release Manager        |
| T5.6    | Testeo de la mensajería Transporte Terrestre              |                36 | Tester                 |
| T5.7    | Implementación de la mensajería Vermas                    |               160 | Desarrollador back     |
| T5.8    | Implementación de Translate Adapter Vermas                |                20 | Desarrollador back     |
| T5.9    | Despliegue de la mensajería Vermas                        |                 8 | Release Manager        |
| T5.10   | Testeo de la mensajería Vermas                            |                16 | Tester                 |
| T5.11   | Implementación de la mensajería Listas Carga/Descarga     |               240 | Desarrollador back     |
| T5.12   | Implementación de Translate Adapter Listas Carga/Descarga |                20 | Desarrollador back     |
| T5.13   | Despliegue de la mensajería Vermas Listas Carga/Descarga  |                13 | Release Manager        |
| T5.14   | Testeo de la mensajería Vermas Listas Carga/Descarga      |                26 | Tester                 |
| T5.15   | Validar requisitos de negocio                             |                25 | Director de negocio    |
| T5.16   | Validar requisitos técnicos                               |                25 | Director de tecnología |
| T5.17   | Puesta en marcha                                          |                40 | Desarrollador back     |
| T5.18   | Pruebas UAT                                               |                20 | Agente Facilitador 1   |
| T5.19   | Soporte y mantenimiento                                   |                50 | Desarrollador back     |

##### 8.5.5.3 Resultados y entregables

| Entregable   | Nombre del entregable                             | Tipo entregable   | Nivel de diseminación   | Mes entrega   |
|--------------|---------------------------------------------------|-------------------|-------------------------|---------------|
| E5.1         | Desarrollo Transporte Terrestre con VP y PORTIC   | Software          | Privado                 | M21           |
| E5.2         | Desarrollo Vermas con VP                          | Software          | Privado                 | M21           |
| E5.3         | Desarrollo  Listas Carga/Descarga con VP y PORTIC | Software          | Privado                 | M21           |

#### 8.5.6 PT6: Análisis del caso de uso 2

##### 8.5.6.1 Objetivos

Analizar los eventos de la plataforma TRADELENS que hoy en día envía el agente facilitador 2 (APV) a través de su PCS ValenciaPortPCS.

##### 8.5.6.2 Descripción del trabajo a realizar

Se realizará un análisis para ver que eventos está enviando APV a TRADELENS. En este caso de uso se tomará como modelo el mismo evento de TRADELENS, que podrá ser utilizado a futuro para otras plataformas que requieran de la integración de estos eventos.

En este paquete se entregará un documento de análisis sobre la integración de la plataforma Translate con la plataforma de TRADELENS.

| Tarea   | Descripción                               |   Horas estimadas | Perfiles requeridos                    |
|---------|-------------------------------------------|-------------------|----------------------------------------|
| T6.1    | Control y seguimiento                     |                14 | Director de proyecto                   |
| T6.2    | Análisis de la mensajería Tradelens       |                80 | Analista 60h, Agente Facilitador 2 20h |
| T6.3    | Análisis de la integración con Translate  |                40 | Analista                               |
| T6.4    | Análisis de la configuración en Translate |                40 | Analista                               |
| T6.5    | Validar requisitos de negocio             |                 5 | Director de negocio                    |
| T6.6    | Validar requisitos técnicos               |                 5 | Director de tecnología                 |

##### 8.5.6.3 Resultados y entregables

| Entregable   | Nombre del entregable                   | Tipo entregable   | Nivel de diseminación   | Mes entrega   |
|--------------|-----------------------------------------|-------------------|-------------------------|---------------|
| E6.1         | Documento de análisis del caso de uso 2 | Documento         | Privado                 | M19           |

#### 8.5.7 PT7: Desarrollo e implementación del caso de uso 2

##### 8.5.7.1 Objetivos

Disponer de una plataforma que integre plataformas como son TRADELENS y ValenciaPortPCS. Una vez hecha esta integración, TRANSLATE puede crecer en más servicios de interoperabilidad ofrecidos a la comunidad portuaria.

El agente facilitador 2 podrá visualizar la auditoría de los eventos enviados a la plataforma de TRADELENS.

##### 8.5.7.2 Descripción del trabajo a realizar

Primero se configurará a la empresa del agente facilitador 2 para que pueda integrar sus eventos con TRADELENS a través de TRANSLATE.

A partir del documento de análisis del PT5, iremos diseñando el modelo a partir de los eventos de TRADELENS.

El agente facilitador 2 tendrá que enviar a Translate los eventos, la plataforma auditará todos los mensajes recibidos y los integrará en TRADELENS.

El agente facilitador 2 tiene que participar en este paquete para poder testear que efectivamente los eventos se envían a la plataforma de TRADELENS.

Una vez puesto en marcha el demostrador, se realizará el mantenimiento operativo del piloto du-rante el periodo requerido.

| Tarea   | Descripción                                   |   Horas estimadas | Perfiles requeridos    |
|---------|-----------------------------------------------|-------------------|------------------------|
| T7.1    | Control y seguimiento                         |                25 | Director de proyecto   |
| T7.2    | Configuración de la empresa en la plataforma  |                20 | Arquitecto             |
| T7.3    | Implementación de la mensajería Tradelens     |               160 | Desarrollador back     |
| T7.4    | Implementación de Translate Adapter Tradelens |                40 | Desarrollador back     |
| T7.5    | Despliegue de la mensajería Tradelens         |                10 | Release Manager        |
| T7.6    | Testeo de la mensajería Tradelens             |                20 | Tester                 |
| T7.7    | Validar requisitos de negocio                 |                 8 | Director de negocio    |
| T7.8    | Validar requisitos técnicos                   |                 8 | Director de tecnología |
| T7.9    | Puesta en marcha                              |                40 | Desarrollador back     |
| T7.10   | Pruebas UAT                                   |                20 | Agente Facilitador 2   |
| T7.11   | Soporte y mantenimiento                       |                50 | Desarrollador back     |

##### 8.5.7.3 Resultados y entregables

| Entregable   | Nombre del entregable   | Tipo entregable   | Nivel de diseminación   | Mes entrega   |
|--------------|-------------------------|-------------------|-------------------------|---------------|
| E7.1         | Desarrollo Tradelens    | Software          | Privado                 | M23           |

### 8.6 Compromisos de facilitación

El proyecto TRANSLATE ha adquirido el compromiso como agente facilitador, suscribiendo los correspondientes acuerdos en los que se establecen las condiciones y compromisos según lo requerido en las bases de Puertos 4.0, de los siguientes operadores del sector logístico-portuario:

- **Autoridad Portuaria de Valencia (APV)** : como organismo público que tiene encomendada la gestión y explotación de los Puertos de Valencia, Sagunto y Gandía, que comportan un nodo fundamental en la concentración y distribución del comercio exterior de la Comunidad Valenciana, en particular, y de su creciente hinterland territorial, en general, con el afán permanente de ofrecer el mejor servicio y atención tanto a sus clientes como al usuario del puerto viene desarrollando, en el marco de su Plan Estratégico, estrategias de innovación tendentes a la facilitación de herramientas de innovación en el entorno de su Comunidad Portuaria, participando activamente en proyectos de impacto positivo en el entorno socioeconómico de los puertos de su competencia consiguiendo con ello estar a la vanguardia de la innovación, especialmente en todo el ámbito de tecnologías emergentes, configurándose además como uno de los puertos más innovadores de Europa, encabezando el ranking de los Top 10 Smart Port del Sistema Portuario Español elaborado por la revista de Ingeniería Civil del Centro de Estudios y Experimentación de Obras Públicas (CEDEX), organismo adscrito orgánicamente al Ministerio de Fomento y funcionalmente a los Ministerios de Fomento y de Agricultura, Alimentación y Medio Ambiente.

La APV considera de enorme interés la ejecución del proyecto TRANSLATE y que se encuentra alineado con sus objetivos estratégicos en materia de innovación.

- **Mediterranean Shipping Company Spain S.L.U. (MSC)** : es una empresa global dedicada al sector del transporte marítimo y la logística. Presente en 155 países, MSC facilita el comercio internacional entre las principales economías del mundo y entre los mercados emergentes de todos los continentes.

MSC hace escala en 500 puertos en 200 rutas comerciales, transportando alrededor de 21 millones de TEU (unidades equivalentes a veinte pies) anualmente, a través de una flota moderna, equipada con las últimas tecnologías ecológicas.

A lo largo de los años, MSC ha diversificado sus actividades para incluir transporte terrestre, logística y una creciente cartera de inversiones en terminales portuarias. Hoy, nuestro enfoque sigue siendo fiel a nuestras raíces y continuamos construyendo y reteniendo alianzas confiables a largo plazo con clientes de todos los tamaños y escalas.

MSC es actual cliente de Infoport de servicios de desarrollo de integración y ha manifestado su interés en ser futuro usuario de la plataforma TRANSLATE.

Es de destacar en este punto la importancia de contar tanto con la empresa MSC como con la APV como agentes facilitadores de la solución, dada su relevancia en el sector logístico-portuario tanto nacional como internacional, lo que sin duda será un elemento clave para el éxito del proyecto.

## 9 Medios y Equipo Emprendedor

### 9.1 Equipo emprendedor

El equipo previsto para el desarrollo del proyecto está formado por personal de **Infoport** con una experiencia contrastada y dilatada en el sector portuario, donde han colaborado con el desarrollo de distintos productos enfocados a Autoridades Portuarias u otras empresas dentro del clúster logístico-portuario, conforme se ha descrito en más detalle en la presentación de Infoport.

El equipo de trabajo de intraemprendimiento, con mayor o menor grado de participación, estaría formado por los siguientes perfiles:

- **Director de Negocio** : Supervisor del plan de negocio y de todos los aspectos estratégicos relacionados con el mismo, así como de verificar que los resultados están alineados con lo previsto en el plan de negocio. En la fase de lanzamiento al mercado, realiza el seguimiento de la cuenta de resultados, flujos de caja, y en general, alinea la estrategia con el plan de negocio. Supervisará las tareas comerciales, de marketing y ventas para alcanzar los objetivos previstos.
- **Director de Tecnología** : Supervisor del cumplimiento del plan de implantación y de todos los aspectos técnicos relacionados con el mismo. Responsable de actuar como facilitador para el cumplimiento de los planes definidos, canalizar la gestión del cambio, análisis de riesgos, comunicación y consecución de los objetivos marcados.
- **Director de Proyecto** : Responsable de liderar el equipo de proyecto con la función de conseguir los objetivos especificados para el producto. Será el encargado del planeamiento y ejecución del Plan de Implantación de la plataforma para la consecución del TRL7. Hará seguimiento del plan de desarrollo y posterior despliegue para el prototipo, aplicando metodologías *agile* .
- **Arquitecto software y cloud** : Responsable del análisis y diseño de la arquitectura software de la plataforma TRANSLATE. Especialista en framework, arquitectura y soluciones en cloud; encargado de la definición de la arquitectura para el despliegue de la solución. Supervisa las infraestructuras como servicio y define las herramientas y soluciones necesarias. Organiza los componentes, las interfaces y las relaciones entre todos que den respuesta a los requerimientos funcionales y no funcionales descritos en el Backlog de producto. Preparación de los entornos para desarrollo e integración continua.
- **Arquitecto analista de datos** : Interpreta datos e información, establece modelos y patrones y define agrupaciones para orquestar el funcionamiento de los sistemas y los modelos de integración, dando coherencia a la información y asegurando su explotación.
- **Analista funcional** : Encargado del análisis funcional de la plataforma en base al alcance definido, proporcionando al equipo de desarrollo la información y documentación necesaria para alinearse con el alcance y el plan de desarrollo y posterior despliegue del prototipo.
- **Release Manager** : Especialista encargado del despliegue de las soluciones sobre la arquitectura definida en cloud. Responsable de establecer los procedimientos que aseguren la calidad de las entregas del prototipo.
- **Técnico de testing** : Responsable de las tareas de pruebas y testeo de la aplicación conforme a los requerimientos de negocio resultantes del análisis funcional. Especialmente importante la documentación de pruebas y resultados en el despliegue del prototipo enfocados a los resultados a presentar.
- **Desarrolladores Back-end** : Desarrolladores en tecnología .netcore encargados del desarrollo de la parte back del aplicativo, en base a la funcionalidad resultante del análisis y de la base de datos y arquitectura diseñada.
- **Desarrolladores Front-end** : Desarrolladores en tecnología Angular encargados del desarrollo de la parte front del aplicativo, y, por tanto, de todo el entorno web, dotando a la plataforma de la funcionalidad resultante del análisis.

Este equipo intervendrá en el desarrollo de la plataforma TRANSLATE hasta la realización y presentación del prototipo. Para la fase de lanzamiento al mercado posterior al proyecto, los perfiles necesarios, adicionales a los anteriores y NO INCLUIDOS en el presupuesto, serían:

- **Especialistas de Soporte** : Equipo de soporte y mantenimiento del software, especializado en la plataforma TRANSLATE y en los servicios de mensajería asociados con la misma. Dimensionado en función del volumen de potenciales clientes de la plataforma, para garantizar un soporte de alta calidad.
- **Comercial y Marketing** : Equipo comercial reforzado para la consecución de los objetivos comerciales marcados para el lanzamiento de la plataforma TRANSLATE al mercado. Encargado de realizar las tareas de ventas y marketing que se estimen necesarias para facilitar el crecimiento esperado de la solución.

| EQUIPO PROPUESTO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre:         José Oliver Murillo  Perfiles:          Director de Negocio  Dedicación en el proyecto: 103 horas  Coste/hora: 55 €  Formación: Licenciado en Informática por la Universidad Politécnica de Valencia desde 1998 además de Executive Máster en Dirección de Empresas.  Además de la Licenciatura en Informática y Executive Máster, ha complementado su formación realizando distintos cursos obteniendo las certificaciones de ITIL y OKR (  *Objectives and Key Results*  ).  En 2004 inició su trayectoria profesional en la empresa consultora Accenture dirigiendo proyectos de consultoría e integración de sistemas para operadores de telecomunicaciones. En 2005 se incorporó a Infoport Valencia, S.A. para coordinar el área de desarrollo y productos software. Posteriormente, en 2009 asumió la Dirección Técnica en Infoport Valencia, S.A. coordinando las áreas técnicas de la compañía, asumiendo, ese mismo año, la Gerencia de la empresa. Como Gerente de Infoport Valencia, S.A. es responsable de la definición de la estrategia de la empresa, así como del seguimiento de objetivos de la compañía supervisando la dirección técnica, comercial, financiera y de personal.  Experiencia profesional: 18 años                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Nombre:         Ángel González Tenorio  Perfiles:          Director de Tecnología  Dedicación en el proyecto: 112 horas  Coste/hora:  42 €  Formación: Ingeniero Superior de Telecomunicaciones por la Universidad Politécnica de Valencia desde 1993.  Además de la Ingeniería Superior de Telecomunicaciones, ha complementado su formación realizando distintos cursos obteniendo las certificaciones con las certificaciones de ITIL, OKR (  *Objectives and Key Results*  ), y  *PRINCE2® FOUNDATION: Certificate in Project Management*  .  Ingeniero superior con amplia experiencia en la dirección de proyectos en el sector de las tecnologías de la información.  En 1999 inició su trayectoria profesional en la empresa Grupotec donde permaneció 13 años ejerciendo inicialmente como consultor SAP y posteriormente como director de proyectos y CIO. Desde 2013 hasta 2015 trabajó en el Grupo Sothis como Director de Marketing y Comunicación externa. Entre los años 2015 y 2019 asumió la dirección de proyectos TIC en las empresas  *The White Team Consulting,*  Grupo Giró, Nunsys y Gesvatec.  En el año En 2020 se incorpora a Infoport Valencia, S.A. como Director Técnico coordinando las áreas técnicas de la compañía (desarrollo y productos software, innovación, sistemas y operación).  Experiencia profesional: 23 años                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Nombre:           Miguel Ángel Portugués Ros  Perfiles:            Director de Proyecto  Dedicación en el proyecto: 449 horas  Coste/hora: 35 €  Formación: Ingeniero Superior de Telecomunicaciones por la Universidad Politécnica de Valencia desde 1996, es además Licenciado en Ciencias Ambientales con un Máster en Innovación Tecnológica.  Además de la Ingeniería Superior de Telecomunicaciones y del Máster en Innovación, ha complementado su formación realizando distintos cursos obteniendo las certificaciones con las certificaciones de ITIL, OKR (  *Objectives and Key Results*  ),  *Scrum Master, Innovation Management, Design Thinking*  e ISO 22301 Continuidad de Negocio.  Posee gran experiencia en la dirección de proyectos en el sector logístico portuario y coordinación de proyectos de I+D+I nacionales e internacionales en los ámbitos de intermodalidad, seguridad de la cadena de suministro, control de accesos, análisis de riesgos e Intelligent Transport Systems (ITS).  Inició su trayectoria profesional en el año 1998 trabajando para la empresa Indra como ingeniero de proyectos. Entre 1999 y 2007 trabajó en Tissat donde desempeñó funciones inicialmente como ingeniero y consultor de proyectos y finalmente como director de proyectos y producto en el sector TI. En el 2007 se incorporó a Infoport como responsable de Ingeniería y Sistemas asumiendo desde el año 2020 la dirección del área de Innovación de la compañía encargándose de la elaboración y ejecución del Plan de Innovación, así como la gestión de la cartera de proyectos de innovación.  Experiencia profesional: 24 años                                                                                                                                                                                                                                              |
| Nombre:          Miguel Albert Vilanova  Perfiles:           Arquitecto software y cloud/Arquitecto de datos  Dedicación en el proyecto: 660 horas  Coste/hora:  30 €  Formación: Ingeniero en Informática por la Universidad Politécnica de Valencia desde 2001.  Además de la Ingeniería en Informática, ha complementado su formación realizando distintos cursos obteniendo la certificación de  *Scrum Master*  y otras específicas de Microsoft.  Ingeniero que inició su trayectoria profesional en 2001 en la empresa IECISA donde permaneció hasta el año 2007. En IECISA ejerció inicialmente como analista programador evolucionando a jefe de equipo de desarrollo realizando la planificación y seguimiento de los trabajos de análisis de requisitos, identificación de necesidades con clientes, diseño de aplicaciones, diseño de arquitecturas software, programación y diseño de base de datos. En 2007 se incorpora a Infoport como analista programador participando en el análisis de numerosos proyectos, especificación de arquitecturas, mantenimiento de arquitecturas, definición de componentes de desarrollo, preparación de prototipos de la solución y validación de desarrollos.  Posee amplia experiencia en análisis y diseño de arquitectura software. Es especialista en framework, arquitectura y soluciones en cloud; definición de arquitectura para despliegues. Ha supervisado infraestructuras como servicio definiendo herramientas y soluciones necesarias. Ha organizado componentes, interfaces y relaciones en base a los requerimientos Ha preparado entornos para desarrollo e integración continua.  Como arquitecto de datos posee amplia experiencia en la interpretación de datos e información, definición de modelos y patrones para orquestar el funcionamiento de los sistemas y los modelos de integración.  Experiencia profesional: 21 años |
| Nombre:          Salvador Navarro García  Perfiles:           Analista funcional/Arquitecto analista de datos  Dedicación en el proyecto: 661 horas  Coste/hora: 21 €  Formación: Técnico Superior en Desarrollo de Aplicaciones Multiplataforma desde 2016. Ha complementado su formación realizando distintos cursos obteniendo la certificación de  *Scrum Master*  y otras específicas de Microsoft.  Se incorporó a Infoport Valencia, S.A. en 2016 y desde entonces ha participado en numerosos proyectos de desarrollo de aplicaciones específicas para el sector de la logística y transporte portuario como analista.  Experiencia profesional: 11 años                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Nombre:          Elena Caballero Seguí  Perfiles:           Técnico de Testing/Release Manager  Dedicación en el proyecto: 446 horas  Coste/hora: 21€  Formación: Ingeniero Técnico en Informática, especialidad Gestión, por la Universidad Politécnica de Valencia desde 1998. Ha complementado su formación realizando distintos cursos obteniendo la certificación de  *ITIL Foundations*  y  *Scrum Master*  .  Inició su trayectoria profesional como programador en distintos sectores como la construcción y producción. Se incorporó a Infoport Valencia, S.A. en 2004 como analista programador participando en distintos proyectos de desarrollo y mantenimiento de aplicaciones de gestión para el sector de la logística portuaria. Ha liderado el testing en las aplicaciones de desarrollo encargándose de la planificación, realización de pruebas e identificación de riesgos de errores de software. Posee experiencia en el despliegue de las soluciones sobre la arquitectura.  Experiencia profesional: 24 años                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Nombre:          Antonio Maiques Magraner  Perfiles:           Desarrollador back - end  Dedicación en el proyecto: 1.100 horas  Coste/hora: 20€  Formación: Ingeniero Industrial Superior especialidad mecánica, por la Universidad Politécnica de Valencia desde 2014.  Inició su trayectoria profesional en 2014 como ingeniero de calidad en la empresa Cesa encargándose de la implementación de aplicaciones para mejorar el control de calidad, implementando la metodología LEAN y supervisando los procesos de producción. En 2016 se incorporó a la empresa Sopra Steria como programador.net participando en distintos proyectos.  sectores como la construcción y producción. En 2016 se incorporó a la empresa Sopra Steria como programador participando en distintos proyectos. Se incorporó a Infoport Valencia, S.A. en 2020 encargándose del desarrollo de la parte back de los distintos aplicativos de la plataforma ValenciaportPCS, en base a la funcionalidad resultante de los análisis y de la base de datos y arquitecturas diseñadas.  Experiencia profesional: 8 años                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Nombre:          Santiago Pérez García  Perfiles:           Desarrollador back - end  Dedicación en el proyecto: 1.300 horas  Coste/hora: 20€  Formación: Grado en Ingeniería Informática, por la Universidad Politécnica de Valencia.  Inició su trayectoria profesional en 2017 como programador en la empresa Serfruit encargándose del desarrollo de software de trazabilidad y producción de la empresa. Posteriormente, en 2019 se incorporó a la empresa Roda Ibérica como analista programador de software de sistemas de trazabilidad e integración con la maquinaria de la compañía. En 2021 se incorporó a Infoport Valencia, S.A. encargándose del desarrollo de la parte back de los distintos aplicativos para el sector logístico portuario, en base a la funcionalidad resultante de los análisis y de la base de datos y arquitecturas diseñadas.  Experiencia profesional: 5 años                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Nombre:          Héctor Bueno Enero  Perfiles:           Desarrollador front - end  Dedicación en el proyecto: 680 horas  Coste/hora: 20€  Formación: Técnico Superior Desarrollo de Aplicaciones Multiplataforma. Ha complementado su formación realizando distintos cursos obteniendo la certificación de  *Scrum.*  Inició su trayectoria profesional en 2017 como programador en las empresas consultoras Stratic y Avanza desarrollando aplicaciones web y móviles. En 2020 se incorporó a Infoport Valencia, S.A. como programador front – end desarrollando aplicaciones web del sector logístico portuario.  Experiencia profesional: 5 años                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### 9.2 Medios y recursos técnicos necesarios

Para el desarrollo de la plataforma TRANSLATE, adicionalmente al equipo de trabajo, se requiere de los siguientes medios, que se incorporan valorados en el capítulo **¡Error! No se encuentra el origen de la referencia.** de **¡Error! No se encuentra el origen de la referencia.** :

- **Servicios de infraestructura cloud** : Será necesario contar con una infraestructura de computación en la nube sobre la que se sustentará la plataforma TRANSLATE. Se van a requerir distintos componentes cloud, que se contratarán en forma de suscripción en pago por uso mediante cuota mensual e irán creciendo en funcionalidad y capacidad con el avance previsto del proyecto. La selección del proveedor cloud más adecuado para alojar la plataforma PaaS será objeto de estudio durante la fase de análisis de la solución en la nube.
- **Formación blockchain:** Para los componentes blockchain a utilizar para el desarrollo de la plataforma TRANSLATE, es necesario considerar acciones formativas específicas para obtener la capacitación técnica necesaria acerca de la plataforma y componentes a incorporar a la arquitectura.

## 10 Plazo de implementación del proyecto

A continuación, se muestra en un cronograma general el plan para la implementación del proyecto, que incluye todas las fases, paquetes de trabajo, hitos, entregables y sus plazos asociados, tal como se han detallado en el *apartado 0*

*Plan para la realización del prototipo en* entorno real

.

El proyecto se ha planificado en un **plazo de ejecución de 24 meses** y se divide en **2 fases** :

- **Fase 1** : Desarrollo de la plataforma PaaS (de mes 1 a mes 16)

- El hito final de esta fase será la disponibilidad de la plataforma base de TRANSLATE en cloud (H1, mes 16).
- En esta fase se ejecutarán los paquetes de trabajo PT1, PT2 y PT3 y se producirán sus entregables asociados.
- El cronograma de la fase1 es el siguiente:

<!-- image -->

- **Fase 2** : Desarrollo de los demostradores de MSC y APV (de mes 13 a mes 24)
- Esta fase tendrá dos hitos:
    - Disponibilidad del demostrador del caso de uso 1, de MSC (H2, mes 24).
    - Disponibilidad del demostrador del caso de uso 2, de la APV (H3, mes 24)
- En esta fase se ejecutarán los paquetes de trabajo PT4, PT5, PT6 y PT7 y se producirán sus entregables asociados.
- El cronograma de la fase2 es el siguiente:
<!-- image -->

## 11 Presupuesto

### 11.1 Resumen del presupuesto

En este apartado se detalla el presupuesto necesario para la ejecución del proyecto hasta la entrega y presentación del prototipo que lleve a **TRANSLATE** a un grado de madurez TRL7.

En la siguiente tabla se resume el presupuesto global. Se considera que **el 100% del presupuesto del proyecto planteado para la plataforma TRANSLATE tiene componente innovadora y es subvencionable** puesto que todas las actividades de desarrollo tecnológico planteadas, tal como se han descrito en la presente memoria técnica, son de carácter innovador, no existiendo solución similar en el mercado actualmente.

<!-- image -->

El **presupuesto estimado total asciende a 189.892 €**

Para la ejecución del proyecto, el esquema de financiación previsto es el siguiente:

- 50% a partir de la subvención solicitada al fondo Puertos 4.0
- 50% a partir de fondos propios.

Actualmente el proyecto no cuenta con ninguna financiación comprometida, ni hay otras ayudas solicitadas para el mismo.

En los siguientes subapartados se detallan las partidas para la que hay una previsión de coste.

### 11.2 Costes de personal

En la siguiente tabla se detallan los costes/hora por perfil para el personal del equipo de proyecto, basados en el cálculo a partir de los costes salariales y con arreglo al convenio colectivo de aplicación:

| **PERFIL**             | **COSTE/HORA**   |
|------------------------|------------------|
| Director de negocio    | 55,00 €          |
| Director de tecnología | 42,00 €          |
| Director de proyecto   | 35,00 €          |
| Arquitecto             | 30,00 €          |
| Analista               | 21,00 €          |
| Desarrollador back     | 20,00 €          |
| Desarrollador front    | 20,00 €          |
| Release Manager        | 21,00 €          |
| Tester                 | 21,00 €          |

A continuación, se incluye el desglose de los costes de personal por paquete de trabajo y tarea, a partir de la dedicación estimada a cada uno y los perfiles requeridos en cada caso:

<!-- image -->

<!-- image -->

### 11.3 Costes de investigación contractual y conocimientos técnicos

Se ha incluido como costes directos la contratación de dos servicios que entendemos importantes para garantizar los trabajos y planificación prevista:

1. Subcontratación de un servicio externo para el desarrollo y soporte en blockchain, por un importe de 15.000 €. El detalle de esta subcontratación se desarrolla en el *apartado 12 Desglose y justificación de subcontrataciones.*
2. Formación en tecnología blockchain, por un importe de 1.500 €, a realizar durante el primer año del proyecto. El detalle de esta formación se describe en el *apartado 9.2*
3. *Medios y recursos técnicos* necesarios.

El total de esta partida asciende a 16.500 €, desglosados del siguiente modo:

<!-- image -->

### 11.4 Gastos generales

La partida de gastos generales incorpora los siguientes conceptos:

- Viajes y dietas, previsto para los desplazamientos necesarios en el proyecto, dedicados a acciones de difusión y presentación de los resultados, por un importe total de 5.000 €
- Asistencia a congresos y seminarios, donde se realizarán conferencias y presentaciones de los demostradores y la plataforma TRANSLATE. El importe de esta partida es de 4.000 €.
- Se incorpora la contratación de una auditoría externa como soporte al control presupuestario y seguimiento del proyecto, que garanticen su correcta ejecución. Se proponen dos controles de auditoría, cada uno por un importe de 1.400 €, en función del avance del plan: el primero tras finalizar el hito 1 disponibilidad de la plataforma base de TRANSLATE en cloud, y el segundo a la finalización del proyecto (hitos 2 y 3).

El total de esta partida asciende a 11.800 €, desglosados del siguiente modo:

<!-- image -->

### 11.5 Gastos en prototipos y pilotos

En esta partida se ha incluido el coste de los gastos de suscripción a los servicios de infraestructura cloud, necesarios para desplegar el demostrador de la plataforma TRANSLATE, tal como se describe en el apartado *apartado 9.2*

*Medios y recursos técnicos* necesarios. El importe previsto es de 6.000 €, a distribuir entre las dos anualidades del proyecto (2.000 € el primer año y 4.000 € el segundo).

### 11.6 Costes indirectos

La partida de costes indirectos se establece en un 20% de los costes de personal, conforme a la realidad contable actual de **Infoport** , siendo imputados a la actividad descrita de forma proporcional, en la parte que razonablemente corresponde de acuerdo con los principios y normas de contabilidad generalmente admitidos y, en todo caso, en la medida en que tales costes corresponden al periodo en que efectivamente se realiza la actividad.

## 12 Desglose y justificación de subcontrataciones

Para el desarrollo del proyecto y la presentación del prototipo de la plataforma TRANSLATE, disponemos prácticamente de todos los recursos internos de personal especializados que permitan llevarlo a cabo. No obstante, se ha considerado necesario incluir en el presupuesto la subcontratación de una empresa especializada en diseño y desarrollo de blockchain, que permita aprovechar al máximo esta tecnología y su uso en la plataforma.

Los requisitos generales que se pretenden cubrir con esta subcontratación son los siguientes:

- Determinar los procesos de la plataforma que requieran certificaciones como intermediarios.
- Diseñar los requisitos de estos procesos a cubrir mediante tecnología blockchain.
- Asesorar acerca de la legislación vigente aplicable a las transacciones, en particular respecto a la seguridad y privacidad de la información.
- Detallar la configuración e implantación de la plataforma blockchain más adecuada de acuerdo a los requisitos técnicos.
- Colaborar en el despliegue de la plataforma blockchain.

La empresa que se encargue de la asesoría blockchain deberá aportar los siguientes perfiles especializados:

- Arquitecto blockchain: capacitado para el análisis y diseño técnico de la plataforma blockchain, definir las mejores prácticas en arquitecturas blockchain, diseñar los smart contracts y las políticas de seguridad a implementar en la red blockchain y desplegar la red blockchain, asegurando la calidad de los trabajos técnicos.
- Desarrollador blockchain: desarrolla las historias de usuario definidas en el product backlog en los componentes de desarrollo de smart contracts e integración de blockchain con el resto de componentes back-end de la solución.

En concreto, la tarea del plan de trabajo que será subcontratada (parcialmente) a esta empresa especializada será la T3.4 Implementación de la integración con blockchain.

Si el proyecto es aprobado y recibe financiación por parte del fondo Puertos 4.0, se abrirá un proceso de petición de ofertas dirigido a las empresas que cubran los requisitos de solvencia técnica y económica necesarios.

El presupuesto previsto para esta colaboración es de 15.000 €.

## 13 Certificados de apoyo

En el Anexo I se incluyen las cartas de apoyo de las siguientes entidades y empresas del sector:

- **Autoridad Portuaria de Málaga:** organismo gestor del Puerto de Málaga, por el que transitan todo tipo de mercancías, tanto los graneles sólidos como los  graneles líquidos y la mercancía general en sus distintos aspectos, carga rodada, vehículos de importación y mercancía contenerizada, cubriendo todas ellas rutas comerciales del arco mediterráneo y atlántico, incluyendo un firme posicionamiento en las líneas de cabotaje con Melilla y Ceuta. También destaca el tráfico de pasajeros de cruceros turísticos con itinerarios programados tanto en el Mediterráneo como en el Atlántico por las principales navieras de este ámbito.

El interés de la AP de Málaga en TRANSLATE se basa en la disponibilidad de servicios de interoperabilidad entre los sistemas del puerto con los distintos operadores económicos, para lo que ha decidido prestar su apoyo al proyecto y mostrar su interés en los resultados.

- **Autoridad Portuaria de Santa Cruz de Tenerife** : es un ente público dependiente de Puertos del Estado que gestiona seis puertos de interés público en la provincia de Santa Cruz de Tenerife (Santa Cruz de Tenerife, Santa Cruz de La Palma, Los Cristianos, San Sebastián de La Gomera y La Estaca). Trabaja de manera activa en las necesidades reales de la Comunidad Canaria integrando tanto los Servicios Portuarios como el espacio físico donde se desarrolla su actividad con actividades de alto impacto económico, social y medioambiental.

El puerto de Santa Cruz de Tenerife está muy interesado en TRANSLATE, siendo un apoyo importante de cara al futuro compromiso de lanzamiento al mercado con el objetivo de dar cobertura a todos los puertos a nivel nacional, para lo cual han manifestado su apoyo.

- **Autoridad Portuaria de Marín** : La Autoridad Portuaria está inmersa en el desarrollo del Plan Estratégico para el Puerto de Marín con un horizonte temporal 2019-2023, considerando el régimen jurídico e institucional, las novedades legislativas y de planificación comunitaria, el contexto socioeconómico así como la realidad actual del Puerto, sus tráficos, sus clientes actuales y potenciales, su papel como generador de valor y su posicionamiento competitivo.

Entre las líneas estratégicas del Puerto de Marín a las que el proyecto TRANSLATE puede contribuir se encuentran la operativa portuaria eficaz y competitividad en los servicios, el papel del puerto en su entorno social y económico y la optimización de recursos tecnológicos.

- **Interglobo Forwarders:** es una empresa multinacional italiana de carga y logística internacional. La compañía ha desarrollado una red global de oficinas que operan en los cinco continentes, sirviendo a diversos mercados clave con servicios altamente personalizados. Los avances tecnológicos siempre han sido un foco principal para el crecimiento de Interglobo, como pieza fundamental para optimizar la eficiencia operativa y la experiencia del cliente.

Interglobo es un cliente al que Infoport presta diferentes servicios de TI, y que ha mostrado su interés en disponer de una plataforma como TRANSLATE.

- **Plataforma Logística Portuaria** : operador de transporte y agente marítimo, operan principalmente en el puerto de Sagunto. Gestionan la exportación e importación de todo tipo de carga: recepción, documentos de despacho, envío, trincaje y todos los procedimientos relacionados con el transporte marítimo, incluyendo la atención al armador y los servicios generales del buque.

Para Plataforma Logística Portuaria, el proyecto TRANSLATE supondrá una mayor facilidad para mantenerse al día en los cambios y las adaptaciones a la mensajería con los PCS.

- **Roca Monzó** : agencia que se dedica a la consignación de toda clase de buques, además del despacho de mercancías de exportación e importación con un servicio puerta a puerta. La empresa se encarga de resolver el transporte marítimo de cualquier carga a cualquier destino, siendo además agentes I.A.T.A. para el tráfico aéreo,

Roca Monzó está interesado en los resultados de TRANSLATE como actual cliente de desarrollos de integración y futuro usuario de la plataforma TRANSLATE de convertirse en una realidad.

## 14 Plan de Negocio

### 14.1 Resumen Ejecutivo

Se realiza en primer lugar un ***Business Model Canvas*** que represente de forma resumida y clara los aspectos principales del proyecto y la idea de negocio:

| **Socios clave**  - **Puertos y PCS** - **Plataformas digitales logísticas**                                                                                                           | **Actividades Clave**  - **Desarrollo plataforma** - **Habilitación blockchain** - **Servicio de soporte**   | **Propuesta de Valor**  - **Facilitar la interoperabilidad de los operadores logísticos** - **Resolver la complejidad existente** - **Mejoras en tiempos de operación logística** - **Servicio y soporte especializado**   |                                                                                                                              | **Relación con Clientes**  - **Soporte y Servicio especializado** - **Gestión comercial**                            | **Segmentos de Clientes**  - **Consignatarios** - **Transitarios** - **Operadores Logísticos** - **Agentes de Aduanas** - **Navieras** - **Terminales y depósitos** - **Agencias Marítimas** - **Transportistas** - **Autoridades Portuarias**   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                        | **Recursos Clave**  - **Equipo de desarrollo** - **Plataforma tecnológica** - **Equipo de soporte**          |                                                                                                                                                                                                                            |                                                                                                                              | **Canales**  - **Presentaciones** - **Publicaciones sector** - **Webinars** - **Marketing digital** - **Sitios Web** |                                                                                                                                                                                                                                                  |
| **Estructura de Costes**  - **Infraestructura tecnológica** - **Costes de personal (desarrollo y mantenimiento)** - **Soporte a usuarios/helpdesk** - **Comercialización y marketing** |                                                                                                              |                                                                                                                                                                                                                            | **Fuentes de Ingreso**  - **Pago por suscripción/alta en el servicio** - **Pago por uso: volumen de uso, servicios activos** |                                                                                                                      |                                                                                                                                                                                                                                                  |

La componente innovadora y propuesta de valor del proyecto TRANSLATE, desde el punto de vista del modelo de negocio, radica en que no existe en el mercado ninguna plataforma de interoperabilidad especializada en el sector logístico-portuario que ayude a los operadores a simplificar los requisitos técnicos y de desarrollo, permitiendo a su vez la posibilidad de pago en función del uso de mensajes o servicios activos en la plataforma. El servicio de soporte al cliente asociado con personal especializado en el sector es otra de las componentes diferenciales.

La plataforma TRANSLATE supone, además, evitar desarrollos específicos por cada uno de los operadores logísticos, acortando los tiempos de puesta en marcha de nuevas conectividades y agilizando la logística al evitar o tiempos innecesarios de adaptación de los sistemas propios.

El proyecto consiste principalmente en el desarrollo de la plataforma centralizada, multiempresa y en pago por uso, y los costes se asocian principalmente al equipo de desarrollo inicial necesario para su puesta en marcha más la infraestructura tecnológica. Los costes derivados del equipo de soporte y mantenimiento serán variables en función del uso y crecimiento posterior de la plataforma, y no son objeto de la ayuda solicitada.

El importe global del proyecto del que se solicita la ayuda asciende a ***189.892 euros*** para el desarrollo del proyecto y presentación del prototipo en un plazo máximo de 24 meses. Se considera la totalidad del proyecto como componente innovadora ya que todas las acciones necesarias están relacionadas con el desarrollo y puesta en producción de una plataforma. Adicionalmente, y como se detalla más adelante en el desarrollo del plan de negocio, es necesaria la ayuda del fondo Puertos 4.0 para que esta plataforma pueda convertirse en una realidad y un avance considerable para el sector.

Las verticales tecnológicas a las que aplica el proyecto se resumen en la siguientes:

- Eficiencia logística en el ámbito operacional y de prestación de servicios
- Digitalización de procesos
- Plataformas como Servicio
- Blockchain
- Cloud Computing

Un factor importante es la TIR a 5 años, que determina la viabilidad del proyecto y posible interés de inversores en el mismo. Una vez desarrollados, como se verá en detalle más adelante, los distintos escenarios de ingresos y gastos a 5 años, las cantidades previstas de beneficios año arrojan una TIR del 5% considerando sólo la inversión necesaria disponiendo de la ayuda. Sin la misma, el TIR a 5 años es negativa, de ahí que resulte clave poder disponer de la ayuda para el desarrollo de la plataforma:

<!-- image -->

### 14.2 Contenido

#### 14.2.1 Propósito de la compañía

*“Proporcionar una plataforma de servicios de intercambio electrónico abierta, escalable e interoperable para la logística portuaria”*

#### 14.2.2 Problema

El objetivo es solucionar un problema existente en el sector en cuanto a la integración de mensajes electrónicos de los operadores económicos cuando se tienen que enfrentar a las múltiples plataformas existentes, cada una de ellas con sus particularidades y requisitos diferentes, tanto técnicos como de datos. Este problema supone actualmente desarrollos propios por parte de cada interlocutor y soluciones específicas “ad hoc”, que generan errores evitables y soluciones mal mantenidas y con alto coste de evolución, así como una barrera de entrada para algunos operadores de pequeño tamaño.

#### 14.2.3 Solución

La solución consiste en desarrollar una plataforma común de servicios de intercambio de mensajería abierta, escalable e interoperable:

- **Abierta** : accesible como servicio y en pago por uso a cada operador o empresa del sector que requiera conectividad de mensajes con las plataformas (PCS u otras).
- **Escalable** : la plataforma TRANSLATE está preparada para reaccionar y adaptarse sin perder calidad, siendo capaz de manejar el crecimiento continuo de trabajo de manera fluida, totalmente preparada para absorber cualquier crecimiento. La escalabilidad aplica en tres dimensiones:
    - *Contenido* : Alcance de la funcionalidad en cuanto a mensajes a procesar y servicios asociados.
    - *Beneficiarios* : Solución diseñada para ser escalable en el volumen de clientes, pudiendo incluso partir de un número limitado de usuarios.
    - *Plataformas* : Autoridades Portuarias con sus PCS y otras que se pueden ir incorporando enriqueciendo la solución,
    - *Tecnología* : Capacidad, crecimiento y disponibilidad asegurada gracias a las soluciones de computación en la nube.
- **Interoperable:** en cuanto a la capacidad de comunicación entre distintos sistemas con distintos datos en distintos formatos de modo que la información pueda ser compartida, accesible desde distintos entornos y comprendida por cualquiera de ellos. Esto, además, es parte del propio ADN de la solución TRANSLATE.

#### 14.2.4 El momento

Hasta el momento, existen soluciones en el mercado, incluida la nuestra denominada MERCURY, que facilitan la interoperabilidad con las plataformas, pero siempre basadas en implantaciones locales ( *on premise* ) y sujetas a particularidades concretas y ad hoc de las necesidades de cada plataforma. Alternativamente, algunos de los grandes operadores y actores del mercado tratan de desarrollar las suyas, con esfuerzos importantes y que de forma periódica necesitan replantear y/o revisar.

Entendemos que hay una necesidad en el mercado y una oportunidad de desarrollar una plataforma como TRANSLATE a raíz de la prueba de concepto realizada, a partir de la cual pudimos detectar, de forma generalizada en el mercado, el gran valor que aportaría tener resuelta la mensajería con distintos puertos, inicialmente a nivel nacional, y además con un servicio de soporte conocedor de la problemática y especializado en el sector.

#### 14.2.5 Mercado potencial

En base al modelo de negocio Canvas desarrollado, el segmento de clientes a los que va dirigido la solución es amplio en el sector:

- Consignatarios
- Transitarios
- Operadores Logísticos
- Agentes de Aduanas
- Navieras
- Terminales y depósitos
- Agencias Marítimas
- Transportistas
- Autoridades Portuarias

Para determinar el mercado potencial de la plataforma TRANSLATE, una vez realizado el prototipo detallado en la presente propuesta, partimos de nuestra propia base instalada de clientes con soluciones basadas en **la integración de mensajería** . Estas soluciones, que son locales y ad hoc para cada cliente, vienen funcionado en los clientes desde hace un tiempo sin haber obtenido ninguna alternativa adecuada salvo que sea el desarrollo propio de la solución. Para este caso, desarrollamos el plan de negocio para una base instalada de aproximadamente 40 cuentas en las que, además, disponemos de datos concretos de ingresos y gastos para poder desarrollar el plan.

Por otra parte, y adicionalmente a esta base instalada que se centraliza principalmente en las comunicaciones con Valenciaportpcs. Con la incorporación del puerto de Barcelona y las incorporaciones posteriores de otros puertos nacionales, tendremos nuevos interlocutores interesados en la conectividad que podemos ofrecer, así como proporcionar nuevos servicios a los que ya la utilizan y tenían resuelta la integración necesaria de mensajes por otros medios.

Todo el mercado potencial a nivel nacional, siempre con conexiones también internacionales, lo podemos estimar en unas 1.200 empresas, a partir de cuentas propias activas identificadas en nuestro CRM, donde vemos recorrido de servicios de interoperabilidad logístico-portuaria adicionales a los que planteamos incorporar en un inicio.

#### 14.2.6 Competencia y alternativas

En el mercado actual, detectamos dos tipos de competidores a la plataforma TRANSLATE, aunque en ninguno de los casos, las soluciones de la competencia son similares a lo que plantea la plataforma, sobre todo en cuanto la especialización en el servicio, la simplificación técnica para los operadores económicos y la escalabilidad de la solución:

1. Empresas dedicadas al intercambio de mensajes en formatos estándar (especialmente formatos EDI) de propósito más general. Una de las empresas más importantes en esta actividad radica en Valencia con una actividad muy importante a nivel nacional e internacional. Si bien, la situación de estas empresas en cuanto su participación en la mensajería específica de la Logística Portuaria es muy pequeña, por varios motivos:
    1. La complejidad y particularidad del sector que requiere unos conocimientos y experiencias muy específicos.
    2. No se trata de grandes volúmenes y son mercados potenciales muy concretos.
2. Desarrollos propios del cliente, por sus propios medios o con la colaboración de alguna empresa más especializada, como sería nuestro propio caso con las integraciones ad-hoc. El problema de esta alternativa:
    3. No escalable
    4. Costoso de mantener y poder evolucionar
    5. Mínimo control, monitorización y control de errores
    6. Evolución claramente comprometida

Por estas razones y la no existencia de una competencia con una solución similar, ni siquiera aproximada a la planteada con la plataforma TRANSLATE y dadas los inconvenientes de las soluciones actuales, entendemos la viabilidad de la solución planteada, así como el momento adecuado para su desarrollo.

##### 14.2.6.1 Matriz de competidores

A continuación, desarrollamos la matriz de la competencia analizando varios factores clave para la solución y los comparamos con los dos tipos de competidores que actualmente existen en el mercado, el desarrollo propio por parte del cliente y las empresas especializadas en mensajería de un propósito general.

<!-- image -->

<!-- image -->

#### 14.2.7 Modelo de negocio

El modelo de negocio para la plataforma TRANSLATE, es un modelo negocio basado en el pago por uso de servicios de computación en la nube para servicios de mensajería, que se compone principalmente de dos componentes que generarán una cuota mensual:

- Los servicios de interoperabilidad que se requieran usar en TRANSLATE, tanto en tipos de mensajes como por número de plataformas con las que se quiera interconectar el operador (pago por uso).
- Los servicios propios de adaptación para el side del cliente (en caso de ser necesarios), que se pueden facturar o bien como un “one-off” en función de las horas necesarias o bien como cuota mensual con un compromiso de permanencia de los servicios contratados en la plataforma.

Para la determinación de los precios de los servicios sobre la plataforma TRANSLATE, disponemos de la información de nuestra base instalada actual que pretendemos migrar a la nueva plataforma, incorporando tanto los servicios de mensajería actuales como nuevos servicios de mensajería y de valor añadido en el uso de la solución. Esa base instalada la componen, por un lado, unos veinte clientes de lo que denominamos MERCURY (Solución de mensajería instalada localmente y con integración únicamente el puerto de Valencia) más otras cincuenta cuentas de base instalada con nuestra solución SINTRAPORT para transporte terrestre, que a su vez requiere de un módulo de intercambio de mensajes. Esto nos permite disponer de una base inicial de información para la determinación de precios y de ingresos desde el momento que se ponga en marcha TRANSLATE y se migren las cuentas actuales, además de las que adicionalmente se puedan incorporar a la plataforma.

El servicio planteado con TRANSLATE es un servicio inexistente en la actualidad que además explota las ventajas de la computación en la nube para aprovechar su escalabilidad, fiabilidad y modelo de negocio enfocado al pago por el servicio recibido. Adicionalmente, TRANSLATE supone una innovación también en cuanto al servicio de valor añadido que supone la solución, desde el punto de vista de soporte especializado en el sector, monitorización y auditoría, teniendo además un gran recorrido a futuro para incorporar nuevos servicios.

Para completar los siguientes tres escenarios del análisis PxQ, partimos de los siguientes supuestos:

- El año 0 no existen ingresos, al ser de un año la fecha comprometida para el lanzamiento a mercado a partir de la finalización del prototipo que situará el proyecto en fase TRL7.
- El año 1 (A1) comienza a partir de la fecha de compromiso de lanzamiento al mercado tras la presentación del prototipo, tiempo necesario para llevar al proyecto a un TRL9.
- Para el paso al TRL9 y la comprobación de que la plataforma está disponible para su operación en producción real con clientes, se tiene previsto la migración de clientes que actualmente utilizan la solución MERCURY.
- Para los ingresos, para las dos fuentes de clientes definidas, base instalada (BI) y nuevos clientes (NC), definimos tres tipos (A,B y C):
<!-- image -->

Con estos datos de partida, establecemos supuestos para tres escenarios (estándar, pesimista y optimista), con evolución a 4 años (A1 a A4), en base a número de clientes incorporados en cada año, según los códigos BI/ABC y NC/ABC. Para el escenario pesimista, reducimos la previsión de crecimiento en clientes en un 25% respecto al escenario base y para el escenario optimista, la incrementamos en un 25%.

<!-- image -->

| **Análisis PxQ**         | **Año 1**                            | **Año 2**                                   | **Año 3**                      | **Año 4**                      |
|--------------------------|--------------------------------------|---------------------------------------------|--------------------------------|--------------------------------|
| **Escenario Pesimista:** |                                      |                                             |                                |                                |
| Ingresos                 | **16.800 €**                         | **42.000 €**                                | **70.000 €**                   | **92.800 €**                   |
| Cantidad                 | 6xBI/A 2xNC/A  4xBI/B 1xNC/B         | 4xBI/A 5xNC/A  2xBI/B 3xNC/B  1xBI/C        | 3xBI/A 8xNC/A  5xNC/B  1xBI/C  | 1xBI/A 14xNC/A  5xNC/B         |
| **Escenario Base:**      |                                      |                                             |                                |                                |
| Ingresos                 | **29.600 €**                         | **68.000 €**                                | **108.800 €**                  | **139.200 €**                  |
| Cantidad                 | 7xBI/A 3xNC/A  4xBI/B 2xNC/B  1xBI/C | 4xBI/A 8xNC/A  2xBI/B 4xNC/B  1xBI/C 1xNC/C | 3xBI/A 12xNC/A  6xNC/B  2xNC/C | 2xBI/A 18xNC/A  6xNC/B  2xNC/C |
| **Escenario Optimista:** |                                      |                                             |                                |                                |
| Ingresos                 | **42.400 €**                         | **94.000 €**                                | **150.000 €**                  | **202.400 €**                  |
| Cantidad                 | 7xBI/A 6xNC/A  4xBI/B 4xNC/B  2xBI/C | 4xBI/A 11xNC/A  2xBI/B 6xNC/B  3xNC/C       | 4xBI/A 15xNC/A  8xNC/B  3xNC/C | 25xNC/A  8xNC/B  2xNC/C        |

El modelo de negocio de pago por uso supone acumular a la facturación estimada anual, en base a la tipología de proyectos, la facturación del año anterior. La tabla de detalle para la obtención de estos importes es la siguiente:

<!-- image -->

#### 14.2.8 Equipo

En el *apartado 9 Medios y Equipo Emprendedor* se detallan los perfiles involucrados en la fase pre-comercial para alcanzar el TRL7 y se indican también los perfiles involucrados en el posterior lanzamiento al mercado de la plataforma TRANSLATE. Se incluyen también los CV para estos perfiles.

Algunas consideraciones generales con relación al equipo definido para el lanzamiento al mercado:

- **Desarrollo de negocio** : para ello contamos con el equipo comercial de Infoport al que aplicamos una dedicación a este lanzamiento en concreto.
- **Marketing** : mismo equipo comercial, junto con Dirección Técnica, Dirección General y Calidad para realizar acciones enfocadas a dar conocer la solución. Consistirá en acciones concretas:
    - Publicaciones: Web Infoport, redes sociales, otros medios especializados en el sector.
    - Webinars: de lanzamiento y periódicos para dar a conocer los nuevos servicios que vaya incorporando la plataforma.
    - Generación de contenidos y noticias.
- **Servicio de Soporte** : Disponemos de un servicio de centro de soporte a usuarios con capacidad suficiente para el lanzamiento.
- **Especialistas de Soporte TRANSLATE** : Una de las características principales de la plataforma es disponer de un servicio especializado. Es por tanto uno de los aspectos clave y para el cual se requiere dedicación específica que irá creciendo en cada ejercicio conforme crezca la plataforma.

Los costes indicados se calculan en función de las horas de dedicación estimadas para cada perfil, y se reflejan en la siguiente tabla:

| **Análisis Coste Equipo**           | **Año 0**   | **Año n-1**   | **Año n**   | **Año n+1**   | **Año n+2**   |
|-------------------------------------|-------------|---------------|-------------|---------------|---------------|
| **Comercial**                       |             |               |             |               |               |
| Coste.                              | 12.660 €    | 12.530 €      | 14.618 €    | 15.362 €      | 17.073 €      |
| N.º FTE                             | 0,27        | 0,26          | 0,31        | 0,32          | 0,36          |
| **Marketing**                       |             |               |             |               |               |
| Coste.                              | 3.500 €     | 2.506 €       | 1.462 €     | 1.536 €       | 1.707 €       |
| N.º FTE                             | 0,09        | 0,06          | 0,04        | 0,04          | 0,04          |
| **Centro de Soporte**               |             |               |             |               |               |
| Coste.                              |             | 2.110 €       | 3.759 €     | 4.385 €       | 4.609 €       |
| N.º FTE                             |             | 0,06          | 0,11        | 0,13          | 0,14          |
| **Soporte Especializado TRANSLATE** |             |               |             |               |               |
| Coste.                              | 3.250 €     | 6.265 €       | 8.771 €     | 9.217 €       | 10.244 €      |
| N.º FTE                             | 0,08        | 0,16          | 0,23        | 0,24          | 0,26          |

#### 14.2.9 Finanzas

Debido a la naturaleza del proyecto presentado en fase pre-comercial y que la actividad se engloba dentro de un Área de Aplicaciones de una compañía con distintas áreas de actividad, **Infoport** , no se incluyen análisis de los estados financieros puestos que éstos no pueden disgregarse de la contabilidad completa de la misma. Un análisis a ese nivel, separado de la situación financiero contable de la compañía completa, además a dos años vista de su salida al mercado, a nuestro entender suponen un ejercicio que no aporta valor al plan de negocio presentado. Por este motivo, presentamos únicamente los aspectos operativos, cuentas de pérdidas y ganancias con resultado a nivel de EBITDA y flujos de caja operacionales, dejando fuera del análisis de detalle, aspectos financieros que dependen de la globalidad de la compañía.

##### 14.2.9.1 Pérdidas y ganancias

<!-- image -->

- Se alcanza el punto de equilibrio en el primer semestre del segundo ejercicio de mercado, año 2.
- El modelo de negocio en pago por uso genera recurrencias anuales que se acumulan en años siguientes lo que genera altos porcentajes de crecimiento en los primeros ejercicios, que se estabilizan en el quinto ejercicio.
- La proyección en cuanto a los ingresos es requiere un crecimiento moderado en los costes de las ventas y costes de personal, pudiendo mantener un EBITDA superior al 30% respecto a los ingresos.

##### 14.2.9.2 Flujos de caja

<!-- image -->

- El modelo de negocio en pago por uso implica alinear en gran medida las ventas a nivel de facturación con los ingresos reales en la caja. En cualquier caso, aplicamos una reducción del 15% por servicios cuyos ingresos se trasladen a siguiente ejercicio y el último mes cuyo ingreso se produce a mes siguiente y, por tanto, en siguiente ejercicio.
- En el primer ejercicio se produce un flujo de caja negativo que será cubierto por fondos propios de **Infoport** .
- En el segundo ejercicio, es cuando alcanzamos el punto de equilibrio a nivel contable y también una situación nivelada de caja.
- En los tres siguientes ejercicios, se pone en relieve que el proyecto se financia con sus ingresos mensuales recurrentes,  y la tasa de variación NOF calculada mes a mes se estabiliza en valores razonables.
- Las inversiones en activos que se recogen en la tabla se refieren a las infraestructuras como servicio a contratar y mantener en Azure. En cualquier caso, estas inversiones en infraestructura se han considerado dentro de los costes directos de ventas para los cálculos de la cuenta de resultados y de los flujos de caja.
- A nivel financiero, podrían derivarse otras consideraciones pero que están sujetas a la situación financiera de la compañía en su conjunto y no del proyecto **TRANSLATE** en concreto.
- Lo más relevante es que el negocio en el tercer ejercicio se autofinancia con sus ingresos y ayudaría al crecimiento y mejora de los balances globales y situación financiera de **Infoport** . A 5 años, se genera un TIR del 6%, en caso de recibir la ayuda, lo que hace razonable la inversión en esta línea de negocio.

#### 14.2.10 Visión

Nuestra visión para la plataforma **TRANSLATE** es que se convierta en un actor principal como Hub de integración digital a nivel nacional en el plazo de 5 años, con crecimiento a nivel internacional en los siguientes años ya que, conforme se vaya adecuando el motor de traducciones a nuevos servicios y nuevas plataformas digitales de intercambio de información, aumentará el valor aportado por la plataforma.

La idea central es constituir un servicio de interoperabilidad innovador especializado en el sector, que aporte valor permitiendo a los participantes olvidarse de la tecnología y centrarse en el negocio.

Por otra parte, tenemos el convencimiento de que esta plataforma innovadora con los objetivos comentados, escalable y con capacidad de crecer en servicios y puertos a conectar, tiene todo el sentido y aporta numerosas ventajas operativas a los operadores y a todo el sector.

### 14.3 Riesgos y amenazas

Con el objetivo de minimizar las situaciones que puedan derivar en desviaciones de los objetivos del proyecto, durante todo el ciclo de vida se aplicará una metodología de gestión de riesgos para identificar, evaluar, valorar, prevenir y actuar sobre las circunstancias que puedan suponer una materialización de estos riesgos para eliminarlos o mitigarlos, evitando que alteren los planes del proyecto.

El equipo de proyecto incorporará entre sus funciones tareas de identificación de riesgos, participando en la determinación de las fuentes, categorización, análisis y propuestas de mitigación. El proceso que se aplicará se sintetiza en:

- Identificación riesgos: Consiste en trabajo de identificación de los riesgos e imprevistos que puedan afectar el normal desempeño del proyecto.
- Determinación fuentes y categorización riesgos: Una vez identificado el riesgo, se identifica las fuentes del mismo y se categorizar.
- Definición de parámetros de análisis: Se definen parámetros de probabilidad de ocurrencia e impacto de los mismos para poder gestionarlos.
- Análisis, evaluación y priorización: En función de los parámetros definidos anteriormente los riesgos son analizados, evaluados y priorizados.
- Definición del plan: En base a los datos obtenidos de los análisis previos, se definen planes de mitigación y/o contingencia.
- Ejecución del plan: En base a los planes definidos se llevan adelante las acciones para la gestión y seguimiento de los riesgos.

En la siguiente tabla se relacionan los riesgos identificados para el proyecto y las acciones de mitigación propuestas. Esta tabla se mantendrá actualizada durante todo el proyecto incorporando cualquier nuevo riesgo que se identifique y modificando el impacto o probabilidad, si procede, así como los planes de contingencia.

| ID   | Riesgo                                                                                                                                               | Impacto   | Probabilidad   | Acciones de Mitigación                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R1   | Desviaciones en el plan de producto por los plazos de desarrollo                                                                                     | Medio     | Baja           | El plan de proyecto seguirá una metodología ágil e incremental por iteraciones, con sprints quincenales, que permite la identificación temprana de desviaciones y aplicación de medidas correctoras                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R2   | Desviaciones en el plan de proyecto por retrasos en las validaciones y pruebas con usuarios                                                          | Medio     | Media          | En el inicio de proyecto se creará un comité de seguimiento del proyecto, constituido por representantes de Infoport y los agentes facilitadores, y se acordará la política de validación, con períodos máximos de 1 o 2 semanas. El comité de seguimiento tendrá entre sus funciones la realización de controles periódicos de cumplimiento de esta política.                                                                                                                                                                                                                                                                                                                     |
| R3   | Dificultad para utilizar datos reales de los operadores para las pruebas de integración con las plataformas digitales                                | Alto      | Baja           | Se propone como alternativa el enmascaramiento de los datos considerados sensibles o confidenciales, como pueden ser los relacionados con clientes, proveedores o terceros. Este enmascaramiento asegurará la ocultación de la identidad de cualquier dato personal o confidencial, que será ocultado o reemplazado para las pruebas por datos equivalentes pero no reales.                                                                                                                                                                                                                                                                                                        |
| R4   | Rechazo a los servicios en la nube (  *cloud*  )                                                                                                     | Alto      | Baja           | Las principales razones para descartar estas soluciones son la seguridad de la información y el coste. La seguridad se garantizará con el uso de plataformas de servicios  *cloud*  100% seguras y la aplicación de políticas de seguridad del sistema de gestión de Infoport, certificado en ISO 27001 y el Esquema Nacional de Seguridad (ENS). El coste se adaptará a la tipología y consumos de cada empresa, lo que permitirá a operadores con menor tamaño y utilización utilizar un servicio similar al de operadores de mayor tamaño a un coste asequible. Asimismo, las aplicaciones  *cloud*  ocupan una cuota de mercado cada vez mayor que contribuye a su aceptación. |
| R5   | Dificultad de los sistemas  *legacy*  de los operadores para generar y procesar mensajería electrónica en los formatos aceptados por las plataformas | Bajo      | Alta           | El proyecto TRANSLATE incluye herramientas que actúan como adaptadores y facilitan que los operadores puedan generar los mensajes electrónicos en el formato  *legacy*  de sus sistemas. Estos adaptadores transforman estos formatos en los nativos utilizados por TRANSLATE y el resto de plataformas. La acción de mitigación consistirá en difundir estas capacidades de TRANSLATE a los clientes potenciales en la fase de comercialización.                                                                                                                                                                                                                                  |
| R6   | Que los operadores realicen los desarrollos para interoperar con las plataformas digitales con sus propios medios                                    | Medio     | Media          | Esta es la situación actual en algunos operadores. En estos casos, el esfuerzo y coste en medios técnicos y humanos para el operador es considerable y va en aumento a medida que necesita interoperar con nuevas plataformas y mantener las anteriores. TRANSLATE les permitirá externalizar estos costes, para focalizarse en su actividad principal, y reutilizar componentes con la correspondiente reducción de costes y plazos.  La acción de mitigación consistirá en difundir estas capacidades de TRANSLATE a los clientes potenciales en la fase de comercialización.                                                                                                    |

## 15 Dotación de ayuda requerida

Para el cálculo de la dotación de ayuda requerida se han tenido en cuenta los siguientes supuestos de partida, teniendo en cuenta el Reglamento (UE) nº 651/2014:

- La tipología y tamaño de la empresa (según las características establecidas en el Anexo 1 del reglamento). Infoport se clasifica como MEDIANA EMPRESA.
- La tipología de proyecto según el reglamento europeo. TRANSLATE se puede clasificar como un proyecto de DESARROLLO EXPERIMENTAL.
- La difusión de los resultados del proyecto. Los resultados del proyecto serán ampliamente difundidos, por medio de al menos dos mecanismos:
    - A través de la publicacion y compartición con la comunidad de datos abiertos del proyecto, que serán
    - Mediante acciones de comunicación del proyecto y sus resultados en diferentes medios de comunicación y publicaciones, así como con la presentación del proyecto a través de conferencias y exposiciones en diferentes foros y congresos especializados del sector, como el Hackaton Valenciaport organizado por la APV y la Fundación Valenciaport, los eventos organizados por la plataforma Logistop, el Congreso Latinoamericano de Puertos organizado por la AAPA, etc.

Por tanto, en función de los anteriores criterios, el porcentaje de subvención solicitada al fondo Puertos 4.0 para la componente innovadora del proyecto es del **50% del presupuesto del proyecto** , por un importe total de **94.946 €**

## 16 Plan temporal de pago de la ayuda

A continuación, se detalla el plan temporal de propuesto para el pago de la ayuda solicitada para el proyecto TRANSLATE, que permitirá a Infoport dotar de recursos al proyecto sin suponer riesgos de tesorería para la empresa. El esquema propuesto es el siguiente:

- Pago del 25% de la ayuda requerida (23.736,5 €) al inicio del proyecto (mes 1)
- Pago del 35% de la ayuda requerida (33.231,10 €) tras la consecución de la fase 1 del proyecto (mes 12), tras su correspondiente justificación.
- Pago final del 40% de la ayuda (37.978,40 €) tras la finalización del proyecto, la comprobación técnico-económica de las actuaciones y la emisión de la correspondiente certificación acreditativa del cumplimiento de los fines que justificaron la concesión de la subvención por parte de la Subdirección de Control de Gestión y Auditoría de Puertos del Estado.

Los plazos indicados anteriormente no son vinculantes a los efectos de la aceptación de la ayuda por parte de Infoport, estando abiertos a alternativas y a proporcionar la flexibilidad que se requiera para este plan.

## 17 Compromiso de lanzamiento al mercado

Infoport se compromete a lanzar al mercado la plataforma TRANSLATE **en el plazo de un año** desde la finalización del proyecto para el que solicita ayuda al fondo Puertos 4.0, considerándose que se consigue alcanzar la madurez tecnológica, el objetivo de la ayuda recibida, y el cumplimiento de las condiciones y los plazos establecidos en el Plan de Negocio y en el Plan de gestión de la propiedad intelectual aportados.

## 18 Anexo I: Cartas de apoyo

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Figures

![Figure fig_0](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_0.png)

![Figure fig_1](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_1.png)

![Figure fig_2](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_2.png)

![Figure fig_3](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_3.png)

![Figure fig_4](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_4.png)

![Figure fig_5](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_5.png)

![Figure fig_6](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_6.png)

![Figure fig_7](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_7.png)

![Figure fig_8](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_8.png)

![Figure fig_9](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_9.png)

![Figure fig_10](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_10.png)

![Figure fig_11](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_11.png)

![Figure fig_12](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_12.png)

![Figure fig_13](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_13.png)

![Figure fig_14](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_14.png)

![Figure fig_15](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_15.png)

![Figure fig_16](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_16.png)

![Figure fig_17](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_17.png)

![Figure fig_18](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_18.png)

![Figure fig_19](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_19.png)

![Figure fig_20](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_20.png)

![Figure fig_21](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_21.png)

![Figure fig_22](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_22.png)

![Figure fig_23](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_23.png)

![Figure fig_24](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_24.png)

![Figure fig_25](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_25.png)

![Figure fig_26](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_26.png)

![Figure fig_27](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_27.png)

![Figure fig_28](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_28.png)

![Figure fig_29](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_29.png)

![Figure fig_30](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_30.png)

![Figure fig_31](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_31.png)

![Figure fig_32](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_32.png)

![Figure fig_33](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_33.png)

![Figure fig_34](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_34.png)

![Figure fig_35](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_35.png)

![Figure fig_36](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_36.png)

![Figure fig_37](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_37.png)

![Figure fig_38](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_38.png)

![Figure fig_39](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_39.png)

![Figure fig_40](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_40.png)

![Figure fig_41](assets/Memoria Técnica Proyecto TRANSLATE 2022 (1)/fig_41.png)

<!-- Image extraction failed: No image data available -->
[Image: Figure fig_42]

<!-- Image extraction failed: No image data available -->
[Image: Figure fig_43]
