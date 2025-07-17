from flask import Flask, render_template, request, redirect
from database import get_db_connection, init_db

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    sweets = conn.execute('SELECT * FROM sweets').fetchall()
    conn.close()
    return render_template('sweets.html', sweets=sweets)

@app.route('/add', methods=['POST'])
def add_sweet():
    name = request.form['name']
    category = request.form['category']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])

    conn = get_db_connection()
    conn.execute('INSERT INTO sweets (name, category, price, quantity) VALUES (?, ?, ?, ?)',
                 (name, category, price, quantity))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
