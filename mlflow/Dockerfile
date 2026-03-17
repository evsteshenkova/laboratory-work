FROM python:3.11-slim
LABEL authors="E.V.Steshenkova"

RUN pip install mlflow
EXPOSE 5001
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5001"]