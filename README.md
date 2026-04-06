# Solemne_1
Solemne 1 Diego Schafer / Adrian Garcia

Local (con uvicorn):

Instalar dependencias: uv pip install fastapi uvicorn

Ejecutar: uvicorn main:app --reload

Docker:

Construir: docker build -t fastapi-app .

Correr: docker run -p 8000:8000 fastapi-app

Probar API:

Navegador o Curl: http://localhost:8000/time
