from flask import Flask, jsonify, request
import os
from models import db, Student, Prediction

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db/{os.getenv('POSTGRES_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return jsonify({
        'service': 'backend',
        'status': 'running',
        'endpoints': [
            '/db-check'
        ]
    })


@app.route('/db-check')
def db_check():
    try:
        from sqlalchemy import text
        db.session.execute(text('SELECT 1'))
        return jsonify({'status': 'connected', 'message': 'DB connected!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # временно
    app.run(host='0.0.0.0', port=5000)