from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Ye line miss ho rahi thi aapki file mein
app = Flask(__name__)

# Database Connection Function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gun_shop_db"
    )

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "admin" and password == "1234":
        return redirect(url_for('dashboard'))
    return "Invalid Credentials! <a href='/'>Try again</a>"

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Ab ye database se data uthaye ga
    cursor.execute("SELECT * FROM weapons")
    db_items = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('index.html', items=db_items)

if __name__ == '__main__':
    app.run(debug=True)