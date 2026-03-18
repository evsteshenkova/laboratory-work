FROM python:3.11-slim
LABEL authors="E.V.Stehenkova"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x /app/start.sh

CMD ["sh", "/app/start.sh"]