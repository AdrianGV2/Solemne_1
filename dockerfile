FROM python:3.11-slim AS builder
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY pyproject.toml .
RUN uv venv /venv && \
    uv pip install --no-cache -r pyproject.toml

FROM python:3.11-slim
WORKDIR /app

COPY --from=builder /venv /venv
COPY . .


ENV TIMEZONE_OFFSET=-4

ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
