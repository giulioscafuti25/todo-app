# Importiamo Flask e le funzioni necessarie
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

# Creiamo l'applicazione Flask
app = Flask(__name__)

# Percorso del database
DATABASE = os.path.join(os.path.dirname(__file__), 'todos.db')


# Funzione per ottenere la connessione al database
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Funzione per inizializzare il database e creare la tabella
def init_db():
    conn = get_db()
    conn.execute(
        'CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)'
    )
    conn.commit()
    conn.close()


# Route principale: mostra la pagina con la lista dei task
@app.route("/")
def index():
    conn = get_db()
    todos = conn.execute('SELECT * FROM todos').fetchall()
    conn.close()
    return render_template("index.html", todos=todos)


# Route per aggiungere un nuovo task
@app.route("/add", methods=["POST"])
def add():
    # Prendiamo il testo del task dalla form HTML
    todo = request.form.get("todo")
    # Aggiungiamo il task solo se non è vuoto
    if todo:
        conn = get_db()
        conn.execute('INSERT INTO todos (task) VALUES (?)', (todo,))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))


# Route per eliminare un task tramite il suo id
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    conn = get_db()
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


# Leggiamo la variabile d'ambiente FLASK_ENV per la modalità debug
debug_mode = os.environ.get('FLASK_ENV') == 'development'


# Avviamo il server sulla porta 5000
if __name__ == "__main__":
    init_db()  # Inizializziamo il database all'avvio
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)  # nosec B104
