# Flujo de trabajo — Uso diario del framework

## Principio base
No todo se documenta.
Solo se documenta lo que:
- afecta decisiones
- afecta alcance
- afecta a otros

---

## Cuándo crear un FR
Crear un FR cuando:
- se acuerda una funcionalidad
- se promete algo a un stakeholder
- se detecta una necesidad recurrente

No crear un FR para ideas vagas.

---

## Cuándo crear un NFR
Crear un NFR cuando:
- hay una restricción técnica o legal
- se define una expectativa de calidad
- el incumplimiento tiene impacto real

---

## Cuándo crear un ADR
Crear un ADR cuando:
- se elige entre alternativas
- la decisión no es obvia
- revertirla sería costoso

Si alguien pregunta “¿por qué hicimos esto?”, faltó un ADR.

---

## Cuándo crear un entregable
Crear un entregable cuando:
- algo se da por cerrado
- algo se envía fuera del equipo
- algo tiene versión y fecha

---

## Flujo resumido
`sources/raw/` → `ingested/` → `curated/` → `deliverables/`  
Nunca al revés.
