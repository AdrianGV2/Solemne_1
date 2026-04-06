FROM python:3.11-slim

WORKDIR /app

# Copiamos uv desde su imagen oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copiamos el archivo de configuración primero
COPY pyproject.toml .

# --- CORRECCIÓN AQUÍ ---
# Instalamos las dependencias directamente en el sistema del contenedor
# Esto evita el error de "exit code 2" por falta de entorno virtual
RUN uv pip install --system --no-cache fastapi uvicorn

# Copiamos el resto del código
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
