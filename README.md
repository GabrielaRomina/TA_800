# TA_800

![Imagen de portada](images/Portada.jpg)


Le damos la bienvenida a TA_800, un proyecto desarrollado como parte del último módulo del bootcamp de Data Science de *The Bridge*. Esta aplicación web en Python, que se convertirá en su TA de confianza, utiliza un modelo preentrenado llamado ChatGPT para buscar y brindar la mejor respuesta a la información solicitada por el usuario mediante la combinación de modelos de lenguaje y Google.

<h2 id="Objetivos"> :dart: Objetivos</h2>

- Desarrollar una aplicación en Python que se conecte a la API de OpenAI de GPT para responder a las solicitudes de los usuarios.
- Crear un front-end que permita a los usuarios interactuar con la herramienta.
- Almacenar las preguntas, respuestas y fechas correspondientes en una base de datos desplegada en la nube (AWS).
- Desplegar la aplicación en Docker.

<h2 id="Producto desarrollado"> :abacus: Producto desarrollado</h2>

El repositorio de GitHub contiene los siguientes elementos:

### 1. Aplicación web

La aplicación web se encuentra implementada en Python y se conecta a la API de GPT para proporcionar respuestas a las consultas de los usuarios. El código fuente de la aplicación se encuentra en la carpeta `app`.

### 2. Dockerfile

El archivo `Dockerfile` se incluye para facilitar el despliegue de la aplicación en contenedores Docker.

### 3. Instrucciones de uso

Para utilizar este repositorio, sigue los pasos a continuación:

1. Clona este repositorio en tu máquina local:

   ```shell
   git clone https://github.com/tu-usuario/TA_800.git
   ```

2. Accede al directorio del proyecto:

   ```shell
   cd TA_800
   ```

3. Configura el entorno virtual (se recomienda el uso de entornos virtuales para evitar conflictos con las dependencias):

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instala las dependencias necesarias:

   ```shell
   pip install -r requirements.txt
   ```

5. Inicia la aplicación:

   ```shell
   python app.py
   ```

6. Abre tu navegador web y accede a `http://localhost:5000` para interactuar con la aplicación.

<h2 id="Contribuidores"> :technologist: Contribuidores</h2>

-   [Gabriela Romina Lupas](https://github.com/GabrielaRomina) 
-   [Xavi Albert](https://github.com/XaviAlbert) 
-   [Javier Tejero](https://github.com/javiertejero1) 
-   [Victoria Suárez](https://github.com/Vihelmet) 