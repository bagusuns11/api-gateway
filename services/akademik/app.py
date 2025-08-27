from flask import Flask, jsonify
import mysql.connector
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # Aktifkan metrics Prometheus

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'rootpassword'),
        database=os.getenv('MYSQL_DATABASE', 'akademik_db')
    )
    return connection

@app.route("/")
def index():
    return {"status": "akademik service OK"}

@app.route('/api/akademik/students', methods=['GET'])
def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(students)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
