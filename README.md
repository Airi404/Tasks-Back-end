# Estructura
## El despliegue se divide en dos servicios principales:
- Web (Django + Gunicorn): El corazón de la aplicación.
- Nginx: Actúa como servidor de archivos estáticos y proxy inverso.

### Paso 1: Configuración del Dockerfile
El Dockerfile define cómo se construye la imagen de nuestra aplicación Python:

`FROM python:3.11`
`WORKDIR /app`

#### Instalamos dependencias
`COPY requirements.txt .`
`RUN pip install --no-cache-dir -r requirements.txt`

#### Copiamos el código del proyecto
`COPY . .`

#### Exponemos el puerto interno
`EXPOSE 8000`

### Paso 2:  Docker Compose
El archivo `docker-compose.yml` gestiona el ciclo de vida de los contenedores y la persistencia de datos de la siguiente manera:

#### Servicio Web (Django)
* **Construcción:** Utiliza el contexto del directorio local (`.`) para generar la imagen.
* **Comandos Automáticos:**
    1.  `python manage.py migrate`: Actualiza la estructura de la base de datos.
    2.  `python manage.py collectstatic`: Reúne todos los archivos CSS, JS e imágenes en una carpeta centralizada.
    3.  `gunicorn`: Arranca el servidor de producción WSGI para manejar las peticiones de Python.
* **Volúmenes:** Comparte el volumen `staticfiles` con el contenedor de Nginx para que los archivos sean accesibles externamente.

#### Servicio Nginx
* **Proxy Inverso:** Actúa como puerta de enlace. Recibe las peticiones en el puerto **80** y las redirige internamente al contenedor web en el puerto **8000**.
* **Gestión de Estáticos:** Sirve directamente los archivos de estilos e imágenes desde el volumen compartido, optimizando la velocidad y liberando de carga a Django.

### Paso 3: Cómo ponerlo en marcha
Ponemos el comando `docker-compose up --build`