FROM python:3.11-slim
LABEL authors="E.V.Stehenkova"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]