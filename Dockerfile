FROM python:3.14-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app
ENV PYTHONPATH=/app