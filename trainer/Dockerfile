FROM python:3.11-slim
LABEL authors="E.V.SSteshenkova"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY train.py .
CMD ["tail", "-f", "/dev/null"]