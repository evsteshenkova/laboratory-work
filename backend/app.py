from flask import Flask, jsonify
import psycopg2
import requests
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return jsonify({
        'service': 'backend',
        'status': 'running',
        'endpoints': 'not yet implemented'
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)