# Seminario de Sistemas 1 — Hoja de Trabajo 2 — Grupo 4

Despliegue de APIs en Máquinas Virtuales con Balanceador de Carga en Azure.

## Estructura del repo

- [`python/`](python) — API en Python (Flask), desplegada en **Instancia-1**.
  Expone `/check` (health check) y `/info` (JSON con Instancia/Curso/Grupo).
  Ver [python/README.md](python/README.md) para pasos de despliegue.
- API en JavaScript (Instancia-2) — pendiente (Persona 2).
- Configuración del balanceador de carga (Load Balancer) — pendiente (Persona 3).

## Entregable

Video grupal (máx. 5 min) mostrando ambas instancias, prueba de cada API,
prueba del balanceador y prueba de tolerancia a fallos (deteniendo
Instancia-2). Enlace se entrega en UEDI y Classroom.
