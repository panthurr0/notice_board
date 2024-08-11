FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY . .