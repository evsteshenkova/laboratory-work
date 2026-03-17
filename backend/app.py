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
            '/db-check',
            '/students',
            '/students/<int:id>'
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


@app.route('/api/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students])


@app.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

@app.route('/api/students', methods=['POST'])
def create_student():
    data = request.json
    student = Student(
        name=data['name'],
        distance_km=data['distance_km'],
        grade=data['grade']
    )
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201


@app.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.json

    if 'name' in data:
        student.name = data['name']
    if 'distance_km' in data:
        student.distance_km = data['distance_km']
    if 'grade' in data:
        student.grade = data['grade']

    db.session.commit()
    return jsonify(student.to_dict())


@app.route('/api/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # временно
    app.run(host='0.0.0.0', port=5000)