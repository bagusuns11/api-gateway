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
        database=os.getenv('MYSQL_DATABASE', 'kepegawaian_db')
    )
    return connection

@app.route("/")
def index():
    return {"status": "kepegawaian service OK"}


@app.route('/api/kepegawaian/employees', methods=['GET'])
def get_employees():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
