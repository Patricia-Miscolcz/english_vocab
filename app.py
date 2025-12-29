from flask import Flask, render_template, request, redirect

import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()  # lê o arquivo .env


app = Flask(__name__)

# Conexão com o banco MySQL
def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"), # coloque seu usuário do MySQL
        password=os.getenv("DB_PASSWORD"),  # coloque sua senha do MySQL
        database=os.getenv("DB_NAME")
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    # Se o formulário for enviado
    if request.method == "POST":
        word = request.form["word"]
        meaning = request.form["meaning"]
        example = request.form["example"]

        sql = "INSERT INTO words (word, meaning, example) VALUES (%s, %s, %s)"
        cursor.execute(sql, (word, meaning, example))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")

    # Buscar todas as palavras
    cursor.execute("SELECT * FROM words ORDER BY created_at DESC")
    words = cursor.fetchall()

    return render_template("index.html", words=words)

if __name__ == "__main__":
    app.run(debug=True)