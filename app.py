from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='togrulm',
        password='2304',
        database='mydb'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM my_table')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
