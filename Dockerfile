FROM python:3.11-slim

WORKDIR /app

COPY main.py .
COPY README.md .

RUN apt-get update && apt-get install -y tk && rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]