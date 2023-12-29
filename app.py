import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_connection():
    conn = psycopg2.connect(host = "localhost",
                            database = "EmployeeDB",
                            user = "postgres",
                            password = "password123")

    return conn

@app.route('/')
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(' SELECT * FROM employees')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', employees = employees)

@app.route('/create/', methods = ('GET','POST'))
def create():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        conn = get_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO employees (name, email,phone)'
                    'VALUES (%s, %s, %s)',
                    (name, email, phone))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))    
    
    return render_template('create.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/update/<int:id>')
def update(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees WHERE id=%s',(str(id)))
    employees = cur.fetchall() 
    cur.close()
    conn.close()
    return render_template('update.html', employees = employees)

@app.route('/edit/', methods = ["POST"])
def edit():
    id = request.form.get("id")
    name = str(request.form["name"])
    email = request.form['email']
    phone = request.form['phone']

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('UPDATE employees SET name=%s, email=%s, phone=%s WHERE id=%s',(name, email, phone, str(id)))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM employees WHERE id = %s',(str(id)))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))
