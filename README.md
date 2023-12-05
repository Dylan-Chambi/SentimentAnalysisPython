# Servicio Web de analisis de sentimiento con FastAPI, Spacy, Modelos de Hugging Face y OpenAI

Este proyecto esta diseñado para realizar un análisis de sentimiento de un texto ingresado por el usuario, utilizando un modelo de Hugging Face o de OpenAI, y mostrar los resultados en una página web.

Este servicio web cuenta con 4 enpoints:

- **/status:** Endpoint que muestra el estado del servicio web e información importante

## Datos Personales

- **Nombre:** Dylan Imanol Chambi Frontanilla
- **Código** 55662

## Requerimientos

Asegúrate de tener instaladas las siguientes herramientas y bibliotecas antes de ejecutar el proyecto:

- [Python](https://www.python.org/): 3.10 o superior.
- Requirements.txt: Archivo que contiene todas las bibliotecas necesarias para ejecutar el proyecto.

## Pasos para ejecutar el proyecto

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/Dylan-Chambi/SentimentAnalysisPython.git
   cd SentimentAnalysisPython
   ```

2. **Crear un entorno virtual:**
   ```bash
    python -m venv venv
    ```
    o
    ```bash
    conda create -n venv python=3.10
    ```

3. **Activar el entorno virtual:**
    ```bash
    source venv/bin/activate
    ```
    o
    ```bash
    conda activate venv
    ```
4. **Instalar las bibliotecas necesarias:**
    ```bash
    pip install -r backend/requirements.txt
    cd Frontend && npm install && cd ..
    ```

5. **Colocar datos en los archivos**
    - **backend/.env:** Archivo que contiene las variables de entorno necesarias para ejecutar el proyecto.
        ```bash
        openai_key=
        ```

    - **frontend/.env:** Archivo que contiene las variables de entorno necesarias para ejecutar el proyecto.
        ```bash
        VITE_BACKEN_URL=
        ```

6. **Ejecutar el proyecto:**
    ```bash
    docker compose up
    ```

### Ejemplo de uso (Backend)

- **Endpoint:** http://localhost:8080/status
    - **Method:** GET

- **Endpoint:** http://localhost:8080/sentiment
    - **Method:** POST
    - **Body:**
        - text: "I like ice cream"

- **Endpoint:** http://localhost:8080/analysis
    - **Method:** POST
    - **Body:**
        - text: "I like ice cream"

- **Endpoint:** http://localhost:8000/reports
    - **Method:** GET

- **Endpoint:** http://localhost:8080/analysis_v2
    - **Method:** POST
    - **Body:**
        - text: "I like ice cream"


Tambien se puede probar el servicio web mediante los servicios desplegados en Google Cloud:

- Backend: https://sentimentanalysispython-547kwfnkdq-ue.a.run.app

- Frontend: https://sentimentanalysispython-547kwfnkdq-uc.a.run.app