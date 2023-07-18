<h1 id="Su asistente definitivo: el TA_800"> :gear: Su asistente definitivo: el TA_800</h1>

![Imagen de portada](images/Portada.jpg)


Le damos la bienvenida a TA_800, un proyecto desarrollado como parte del último módulo del bootcamp de *Data Science* de *The Bridge*. Esta aplicación web en Python, que se convertirá en su TA de confianza, utiliza un modelo preentrenado llamado ChatGPT para buscar y brindar la mejor respuesta a la información solicitada por el usuario mediante la combinación de modelos de lenguaje y Google.

<h2 id="Objetivos"> :dart: Objetivos</h2>

- Desarrollar una aplicación en Python que se conecte a la API de OpenAI de GPT para responder a las solicitudes de los usuarios.
- Crear un *front-end* que permita a los usuarios interactuar con la herramienta.
- Almacenar las preguntas, respuestas y fechas correspondientes en una base de datos desplegada en la nube (AWS).
- Desplegar la aplicación en Docker.

<h2 id="Estructura del repositorio"> :file_folder: Estructura del repositorio</h2>

El repositorio de este proyecto contiene los siguientes archivos:

* app.py: archivo principal de la aplicación web.
* Dockerfile: archivo necesario para construir la imagen de Docker.
* docker-compose.yml: archivo de configuración de *Docker Compose* para facilitar el despliegue de la aplicación.
* requirements.txt: archivo que lista las dependencias del proyecto.
* carpetas *templates* y *static*: que contienen los archivos *html* y *css* necesarios para desplegar el front end.
* download_db.py: archivo descargar y visualizar la base de datos actualizada con las últimas consultas en formato .xlsx

<h2 id="Instrucciones de uso"> :key: Instrucciones de uso</h2>

Para utilizar este repositorio, sigue los pasos a continuación:

1. Clona este repositorio en tu máquina local:

   ```shell
   git clone https://github.com/GabrielaRomina/TA_800.git
   ```

2. Accede al directorio del proyecto:

   ```shell
   cd TA_800
   ```

3. Despliega la app en tu cuenta de Docker Hub (¡que no se te olvide el punto del final!):

   ```shell
   docker build -t <nombre_de_usuario>/appgpt_model .
   ```

4. Descarga la imagen creada y ejecútala (recuerda no tener el puerto 5000 en uso y abrir Docker Desktop):

   ```shell
   docker run -p 5000:5000 -d <nombre_de_usuario>/appgpt_model
   ```

5. Sobre la aplicación desplegada, construye tu versión de la app:

   ```shell
   docker build -t <nombre_de_usuario>/appgpt_model:v1.0.0 .
   ```

6. Abre tu navegador web y accede a `http://localhost:5000` para interactuar con la aplicación.

<h2 id="Contribuidores"> :technologist: Contribuidores</h2>

-   [Gabriela Romina Lupas](https://github.com/GabrielaRomina) 
-   [Xavi Albert](https://github.com/XaviAlbert) 
-   [Javier Tejero](https://github.com/javiertejero1) 
-   [Victoria Suárez](https://github.com/Vihelmet) 