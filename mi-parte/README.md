# API Python — Persona 1 — Instancia-1

## Antes de desplegar
1. `CURSO` y `GRUPO` en `app.py` ya están configurados con los datos reales
   (Seminario de Sistemas 1 A, Grupo 4).
2. Prueba local (ya verificado en este entorno):
   ```bash
   python3 app.py
   curl http://localhost:5000/check   # -> 200 OK
   curl http://localhost:5000/info    # -> JSON
   ```

## Archivos
- `app.py` — API Flask con `/check` y `/info`.
- `requirements.txt` — dependencias (Flask, gunicorn).
- `api-python.service` — unidad systemd para correrla como servicio persistente en la VM.

## Despliegue en Azure (Instancia-1)

Elige **uno** de los 3 métodos que permite la hoja de trabajo. El más simple es
clonar el repo de GitHub o subir por SFTP con Termius; abajo están los pasos
para SFTP/clonación + systemd.

1. Crea la VM en Azure Portal: nombre `Instancia-1`, imagen Ubuntu 22.04 LTS,
   tamaño B1s (o el que uses en el curso), abre el puerto **5000** (o el 80 si
   prefieres poner Flask detrás de nginx) en el NSG además de 22 (SSH).
2. Copia esta carpeta a la VM (SFTP con Termius, o `git clone` si subes el
   repo a GitHub):
   ```bash
   scp -r api-python azureuser@<IP_INSTANCIA_1>:/home/azureuser/
   ```
3. Conéctate por SSH e instala dependencias:
   ```bash
   ssh azureuser@<IP_INSTANCIA_1>
   sudo apt update && sudo apt install -y python3-venv
   cd api-python
   python3 -m venv venv
   ./venv/bin/pip install -r requirements.txt
   ```
4. Prueba manual en la VM:
   ```bash
   ./venv/bin/python app.py
   # en otra terminal / desde tu máquina:
   curl http://<IP_INSTANCIA_1>:5000/check
   curl http://<IP_INSTANCIA_1>:5000/info
   ```
5. Deja el servicio corriendo de forma persistente con systemd:
   ```bash
   sudo cp api-python.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now api-python
   sudo systemctl status api-python
   ```
6. Verifica desde tu navegador o `curl` usando la **IPv4 pública** de
   Instancia-1: `http://<IP_PUBLICA>:5000/info`.

## Checklist para Persona 1
- [x] `app.py` con Curso/Grupo reales (Seminario de Sistemas 1 A, Grupo 4)
- [ ] Probado en local (`/check` = 200, `/info` = JSON correcto)
- [ ] VM `Instancia-1` creada en Azure
- [ ] Puerto 5000 abierto en el NSG
- [ ] API desplegada y corriendo como servicio (systemd)
- [ ] `/check` y `/info` responden por la IPv4 pública de Instancia-1
- [ ] IPv4 pública y nombre de la instancia anotados para el video
