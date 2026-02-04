---
title: "Ficha de Proyecto APV – RCCC STS Valenciaport"
version: 1.0
date: 2026-01-29
---

# Ficha de Proyecto – Autoridad Portuaria de Valencia

## Datos generales

**Nombre del proyecto**  
RCCC STS Valenciaport – Centro de Control Remoto para Grúas Ship-to-Shore

**Programa / Convocatoria**  
Programa Ports 4.0 – Modalidad Proyectos Pre-comerciales (Puertos del Estado)

**Nombre del responsable**  
Carlos Alexis Zavala Galarce

**Email del responsable**  
[por completar]

**Nombre de la empresa**  
Infoport Valencia, S.A.

**Web de la empresa**  
https://www.infoport.es

**Vertical principal (Ports 4.0)**  
Seguridad y Protección

---

## Descripción del proyecto

Propuesta de un Centro de Control Remoto para grúas Ship-to-Shore (STS) en Valenciaport, orientado a mejorar la seguridad, la ergonomía del personal y la eficiencia operativa. El proyecto plantea una arquitectura industrial en la que la grúa mantiene un PLC como IO Device para la adquisición/actuación de señales de campo, mientras que la lógica de control y la supervisión HMI/SCADA se desplazan a una sala de control remota.

La solución integra comunicaciones industriales, vídeo de baja latencia para asistencia visual al operador, y un repositorio de datos operativos que permite explotar KPIs y analítica avanzada. El proyecto se plantea inicialmente como piloto pre-comercial acotado a 1 grúa STS en una terminal de contenedores de Valenciaport, con plan de pruebas, modo degradado definido y escalabilidad posterior a operación multi-grúa y a futuros niveles de semiautomatización.

El diseño es compatible y puede beneficiarse de la red privada 5G de Valenciaport en despliegue, como soporte de comunicaciones fiables y de baja latencia para control remoto, vídeo y sensorización avanzada.

---

## Componente innovador

El componente innovador reside en la combinación de:

- Reubicación de la inteligencia de control de la grúa STS desde la cabina física a una sala remota, manteniendo la grúa como IO Device y respetando las arquitecturas industriales y requisitos de seguridad funcional.  
- Uso integrado de vídeo de baja latencia y datos de proceso en tiempo real para soportar operación remota segura y trazable, con registro completo de eventos y maniobras.  
- Generación sistemática de datos operativos estructurados (eventos, estados, tiempos de ciclo, alarmas, etc.) como base para analítica, KPIs y futuras aplicaciones de optimización y semiautomatización.  
- Aprovechamiento de la red privada 5G del puerto como palanca de conectividad avanzada para casos de uso críticos (control remoto, vídeo y sensorización de seguridad) en el entorno portuario.

---

## Tecnología propuesta

Arquitectura basada en tecnologías industriales consolidadas y elementos de nueva generación:

- **PLCs industriales** (PLC controlador en sala de control y PLC IO Device en la grúa) comunicados mediante red industrial (por ejemplo, PROFINET o equivalente) para garantizar baja latencia y fiabilidad en señales de mando y feedback.  
- **Sistema HMI/SCADA** para supervisión en tiempo real, gestión de alarmas, registro histórico y diagnóstico básico, integrado con la lógica de control remoto.  
- **Sistema de vídeo de baja latencia** (p. ej. tecnologías tipo WebRTC u otras soluciones equivalentes) que proporcione al operador una visión completa y segura de la zona de operación.  
- **Base de datos** para almacenamiento de datos operativos y explotación mediante herramientas de BI/analítica (KPIs, cuadros de mando, estudios de productividad y seguridad).  
- **Red privada 5G de Valenciaport** como infraestructura de comunicaciones críticas para vídeo, telemetría y sensorización, en combinación con redes industriales cableadas allí donde sea necesario.  
- **Capa de ciberseguridad OT**, segmentación de redes y control de accesos adaptados al contexto portuario.

---

## Impacto del proyecto

- **Seguridad operacional:** reducción de la exposición directa de los operadores en la zona de grúas STS y mejora de la capacidad de monitorización de riesgos.  
- **Ergonomía y condiciones laborales:** mejora del entorno de trabajo (sala de control versus cabina en altura), reducción de fatiga y potencial incremento de la capacidad para atraer y retener talento especializado.  
- **Eficiencia operativa:** base para reducir tiempos de ciclo y mejorar la fiabilidad operativa al disponer de mejor supervisión, datos de operación y herramientas de diagnóstico.  
- **Gestión basada en datos:** disponibilidad de KPIs y analítica para optimizar la planificación y el uso de recursos (grúas, turnos, apoyo en tierra), además de facilitar comparativas entre operaciones tradicionales y operaciones remotas.  
- **Posicionamiento estratégico:** refuerzo del rol de Valenciaport como puerto de referencia en innovación y en la aplicación de redes 5G privadas y tecnologías 4.0 a la operación de terminales de contenedores.

---

## Principales beneficios

**Para la APV**

- Proyecto emblemático de aplicación de tecnologías 4.0 y 5G en un caso de uso crítico y visible.  
- Mejora de la seguridad operacional y de la imagen de innovación del puerto.  
- Marco replicable a otras terminales y a otros activos portuarios.

**Para terminales y operadores**

- Potencial reducción de incidentes y *near-miss* en operaciones de grúa STS.  
- Mejores condiciones laborales para los operadores y mayor resiliencia operativa.  
- Datos de alto valor para la optimización de productividad y planificación.

**Para el ecosistema (proveedores tecnológicos, centros de I+D)**

- Caso de uso real para validar tecnologías de control remoto, vídeo de baja latencia y ciberseguridad OT.  
- Oportunidad de desarrollar soluciones exportables a otros puertos y terminales.

---

## Beneficiarios

- Autoridad Portuaria de Valencia (APV).  
- Terminal(es) de contenedores participantes en el piloto.  
- Operadores de grúas STS y personal técnico de mantenimiento.  
- Empresas tecnológicas del ecosistema (integradores OT, proveedores de comunicaciones, ciberseguridad, etc.).  
- Navieras y clientes de la terminal, de forma indirecta, al beneficiarse de operaciones más seguras y fiables.

---

## Problema que se resuelve

El proyecto aborda la necesidad de mejorar la seguridad y las condiciones de trabajo en la operación de grúas STS, donde actualmente los operadores trabajan en cabinas en altura, en entornos exigentes y con elevada responsabilidad sobre la seguridad de personas, equipos y mercancía. La falta de datos estructurados de operación de grúas y la dificultad para evaluar de forma objetiva el impacto de cambios operativos limita la capacidad de optimizar productividad y ergonomía.

Asimismo, los puertos se enfrentan al reto de incorporar tecnologías de conectividad avanzada (como redes privadas 5G) a casos de uso críticos, de forma controlada y medible. El proyecto propone un piloto acotado que responde a estos retos combinando control remoto, supervisión, datos y comunicaciones avanzadas.

---

## Equipo y recursos

**Autoridad Portuaria de Valencia (APV)**  
Coordinación institucional del proyecto, alineamiento con la estrategia Ports 4.0, acceso al entorno portuario y a la red privada 5G, relación con terminales y otros agentes.

**Terminal de contenedores participante**  
Definición de requisitos operativos, selección de la grúa STS piloto, participación en diseño de procedimientos de operación remota, pruebas y validación en entorno real.

**Infoport Valencia (u otro integrador tecnológico principal)**  
Liderazgo técnico del proyecto, diseño de la arquitectura de control remoto, integración HMI/SCADA, base de datos y capa de analítica/BI.

**Partner OT / integrador de grúas**  
Adaptación e integración con sistemas de control existentes en la grúa STS, validación de requisitos de seguridad funcional.

**Partner de comunicaciones (5G / redes industriales)**  
Diseño y despliegue de la arquitectura de comunicaciones (red privada 5G + redes industriales cableadas) acorde a los requisitos de latencia y fiabilidad.

**Partner de ciberseguridad OT**  
Definición de la segmentación de redes, control de accesos, monitorización de seguridad y cumplimiento de buenas prácticas en entorno industrial.

**Universidad / centro tecnológico (opcional)**  
Apoyo en metodologías de evaluación, analítica avanzada y documentación de resultados.

---

## Presupuesto estimado

- **Presupuesto total estimado del piloto pre-comercial (1 grúa STS):** 800.000 €  
- **Aportación solicitada a través de Ports 4.0**  
  (Ayuda pre-comercial, hasta ~60 % de la parte innovadora): 480.000 €  
- **Cofinanciación y aportaciones en especie**  
  (terminal, proveedores tecnológicos, APV, etc.): 320.000 €

El detalle por partidas (ingeniería OT, comunicaciones, sistemas HMI/SCADA, vídeo, ciberseguridad, pruebas y gestión del proyecto) se podría desglosar en una hoja anexa.

---

## Apoyo / facilitación solicitada a la APV

Se solicita apoyo de la APV en forma de:

- Carta de apoyo para la propuesta a la convocatoria Ports 4.0 (modalidad pre-comercial).  
- Rol de agente facilitador para articular el piloto con una terminal de contenedores, coordinar el uso de la red privada 5G y facilitar el acceso a interlocutores clave (operación, mantenimiento, seguridad y ciberseguridad).

---

## Razón por la que se solicita el apoyo / facilitación

El proyecto requiere la participación activa de una terminal de contenedores y el uso de infraestructuras estratégicas del puerto (especialmente la red privada 5G), así como el alineamiento con las políticas de seguridad y de ciberseguridad OT de la APV. La APV es el actor mejor posicionado para facilitar la coordinación entre terminales, proveedores tecnológicos y otros agentes del ecosistema, y para dotar al proyecto de la legitimidad necesaria de cara a su presentación a Ports 4.0 y su posterior escalado a otros activos o terminales en el puerto.

---

## Otros apoyos solicitados / otros socios de relevancia

Se prevé solicitar apoyo a la convocatoria Ports 4.0 de Puertos del Estado en modalidad de proyecto pre-comercial, así como la participación de:

- Una terminal de contenedores de Valenciaport como usuario principal del piloto.  
- Empresas integradoras OT y de comunicaciones (incluyendo, en su caso, el operador de la red privada 5G del puerto).  
- Un partner especializado en ciberseguridad OT.  
- Universidad o centro tecnológico (p. ej. UPV) para apoyo en metodologías de evaluación y explotación de resultados.

No se descarta la exploración de otros instrumentos de apoyo regional, nacional o europeo compatibles con el marco de Ports 4.0.