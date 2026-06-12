from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create Database
conn = sqlite3.connect('database.db')
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER,
    attendance INTEGER,
    result TEXT
)
""")
conn.close()


# Home Page
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()

    return render_template('index.html', students=students)


# Add Student
@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']
    marks = int(request.form['marks'])
    attendance = int(request.form['attendance'])

    # Result Logic
    if marks < 40 or attendance < 45:
        result = "Fail"
    else:
        result = "Pass"

    conn = sqlite3.connect('database.db')

    conn.execute(
        'INSERT INTO students (name, marks, attendance, result) VALUES (?, ?, ?, ?)',
        (name, marks, attendance, result)
    )

    conn.commit()
    conn.close()

    return redirect('/')


# Delete Student
@app.route('/delete/<int:id>')
def delete_student(id):

    conn = sqlite3.connect('database.db')

    conn.execute(
        'DELETE FROM students WHERE id=?',
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')


# Edit Page
@app.route('/edit/<int:id>')
def edit_student(id):

    conn = sqlite3.connect('database.db')

    student = conn.execute(
        'SELECT * FROM students WHERE id=?',
        (id,)
    ).fetchone()

    conn.close()

    return render_template('edit.html', student=student)


# Update Student
@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):

    name = request.form['name']
    marks = int(request.form['marks'])
    attendance = int(request.form['attendance'])

    if marks < 40 or attendance < 45:
        result = "Fail"
    else:
        result = "Pass"

    conn = sqlite3.connect('database.db')

    conn.execute(
        'UPDATE students SET name=?, marks=?, attendance=?, result=? WHERE id=?',
        (name, marks, attendance, result, id)
    )

    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
import webbrowser

if __name__ == '__main__':


     webbrowser.open('http://127.0.0.1:5000')

     app.run(debug=True)

