import psycopg2
import mlflow
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

print("Connecting to database...")
conn = psycopg2.connect(
    host='db',
    database=os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD')
)

cur = conn.cursor()
cur.execute('SELECT distance_km, grade FROM students')
data = cur.fetchall()
cur.close()
conn.close()

print(f"Загружено {len(data)} студентов")

if len(data) > 1:
    X = [[d[0], d[1]] for d in data]
    y = [1 if d[0] > 5 else 0 for d in data]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, '/models/model.pkl')

    mlflow.set_tracking_uri('http://mlflow:5001')
    with mlflow.start_run():
        mlflow.log_param('samples', len(X))
        mlflow.sklearn.log_model(model, 'model')

    print("Model trained and saved!")
else:
    print("Not enough data")