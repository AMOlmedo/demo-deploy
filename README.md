# demo-depoly

# Docker Compose en WSL (Ubuntu)

Este documento resume los pasos necesarios para instalar y usar Docker Compose dentro de WSL (Windows Subsystem for Linux), incluyendo solución de problemas y una guía básica para mantener contenedores activos.

---

## Instalación de Docker Compose (moderno)

### 1. Eliminar versiones anteriores (opcional)

```bash
sudo apt remove docker docker.io containerd runc
```

### 2. Actualizar los paquetes del sistema

```bash
sudo apt update
sudo apt upgrade
```

### 3. Configurar repositorio oficial de Docker

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

### 4. Agregar repositorio Docker al sources.list

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 5. Instalar Docker y Docker Compose plugin

```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 6. Verificar la instalación

```bash
docker compose version
```

---

## Problemas comunes en WSL

### Falla al resolver dominios (DNS)

Editar `/etc/resolv.conf` si hay problemas para acceder a `archive.ubuntu.com` u otros dominios:

```bash
cat /etc/resolv.conf
```

Si hay errores, probar reiniciar WSL o cambiar manualmente el nameserver a 8.8.8.8 o 1.1.1.1

```bash
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

**Importante:** Puede ser necesario desactivar la regeneración automática en `/etc/wsl.conf`

```ini
[network]
generateResolvConf = false
```

---

## Ejemplo básico de docker-compose.yml

```yaml
services:
  db-mysql:
    image: mysql
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=12345

  backend:
    image: python
    command: tail -f /dev/null
    ports:
      - "8000:8000"
    volumes:
      - /home/adrian/bunker4/projectFinal/backend:/app

  react-server:
    image: node
    command: tail -f /dev/null
    ports:
      - "3000:3000"
    volumes:
      - /home/adrian/fullstack/react-proyectos/pildorasReact/react-docker:/app
```

---

## Mantener contenedores activos

Agregar la siguiente línea evita que los contenedores se cierren automáticamente al arrancar:

```yaml
command: tail -f /dev/null
```

También se puede usar:

```bash
docker exec -it <nombre_contenedor> bash
```

para acceder a una shell dentro del contenedor.

---

## Comandos útiles

* Levantar servicios:

  ```bash
  docker compose up
  ```
* Levantar en segundo plano:

  ```bash
  docker compose up -d
  ```
* Ver estado:

  ```bash
  docker compose ps
  ```
* Detener:

  ```bash
  docker compose down
  ```

---


