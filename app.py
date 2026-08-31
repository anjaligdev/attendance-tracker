import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form["studentName"]
    school = request.form["studentSchool"]
    batch = request.form["studentBatch"]

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, school, batch) VALUES (?, ?, ?)",
        (name, school, batch)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)