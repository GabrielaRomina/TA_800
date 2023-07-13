# TA_800

# GPT Googler

Bienvenido a GPT Googler, un proyecto desarrollado como parte del último módulo del bootcamp de Data Science. Esta aplicación web en Python utiliza un modelo preentrenado llamado GPT para buscar y brindar la mejor respuesta a la información solicitada por el usuario mediante la combinación de modelos de lenguaje y Google.

## Objetivos

- Desarrollar una aplicación en Python que se conecte a la API de OpenAI de GPT para responder a las solicitudes de los usuarios.
- Crear un front-end minimalista que permita a los usuarios interactuar con la herramienta.
- Investigar las bibliotecas [langchain](https://python.langchain.com/docs/get_started/introduction.html) y [OpenAI](https://platform.openai.com/docs/introduction).
- Almacenar las preguntas, respuestas y fechas correspondientes en una base de datos desplegada en la nube (AWS).
- Desplegar la aplicación en Docker.

## Entregable

El repositorio de GitHub contiene los siguientes elementos:

### 1. Aplicación web

La aplicación web se encuentra implementada en Python y se conecta a la API de GPT para proporcionar respuestas a las consultas de los usuarios. El código fuente de la aplicación se encuentra en la carpeta `app`.

### 2. Dockerfile

El archivo `Dockerfile` se incluye para facilitar el despliegue de la aplicación en contenedores Docker.

### 3. Instrucciones de uso

Para utilizar este repositorio, sigue los pasos a continuación:

1. Clona este repositorio en tu máquina local:

   ```shell
   git clone https://github.com/tu-usuario/gpt-googler.git
   ```

2. Accede al directorio del proyecto:

   ```shell
   cd gpt-googler
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

### 4. Contribuidores

-   [Gabriela Romina Lupas](https://github.com/GabrielaRomina) 
-   [Xavi Albert](https://github.com/XaviAlbert) 
-   [Javier Tejero](https://github.com/javiertejero1) 
-   [Victoria Suárez](https://github.com/Vihelmet) 