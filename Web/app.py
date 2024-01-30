from flask import Flask, render_template, request, redirect, flash, session
import pymysql
import db_init

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/')
def index():
    db_init.sql_init()
    return redirect(request.path + 'login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='test_db')
        cursor = conn.cursor()
        query = f"SELECT username FROM Users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchall()
        return f"Executed Query: {query} <br> Query Result: " + ', '.join(map(str, result))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=False)
