from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    distance_km = db.Column(db.Float, nullable=False)
    grade = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    # Связь с предсказаниями
    predictions = db.relationship('Prediction', back_populates='student', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'distance_km': self.distance_km,
            'grade': self.grade,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Prediction(db.Model):
    __tablename__ = 'predictions'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    risk_score = db.Column(db.Float, nullable=False)
    risk_level = db.Column(db.String(20), nullable=False)
    model_version = db.Column(db.String(50), default='v1')
    created_at = db.Column(db.DateTime, default=datetime.now)

    # Связь со студентом
    student = db.relationship('Student', back_populates='predictions')

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'student_name': self.student.name if self.student else None,
            'risk_score': self.risk_score,
            'risk_level': self.risk_level,
            'model_version': self.model_version,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
