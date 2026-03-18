#!/bin/sh

echo "Ожидаем подключение к БД..."

while ! python -c "import os, psycopg2; psycopg2.connect(host='db', database=os.getenv('POSTGRES_DB'), user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD')).close()" 2>/dev/null
do
  echo "БД не загрузилась.."
  sleep 2
done

echo "БД загрузилась - запускаются миграции"
alembic upgrade head

echo "Запуск бэкенд сервиса"
python app.py