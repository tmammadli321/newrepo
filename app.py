from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, template_folder='./templates', static_folder='./static')

@app.route('/', methods=['GET'])
def get_data():
    conn = mysql.connector.connect(
        host='localhost',
        user='togrulm',
        password='2304',
        database='mydb'
    )
    cursor = conn.cursor(dictionary=True)  # Use dictionary=True to get column names
    cursor.execute('SELECT * FROM my_table')
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
