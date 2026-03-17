# РЕАЛИЗОВАНО ИСКЛЮЧИТЕЛЬНО ДЛЯ ТЕСТИРОВАНИЯ СЕРВИСА!

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    distance_km FLOAT,
    grade FLOAT
);

INSERT INTO students (name, distance_km, grade) VALUES
    ('Иван Петров', 0.5, 4.8),
    ('Мария Иванова', 12.0, 2.5);