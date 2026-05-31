# Importiamo Flask e le funzioni necessarie
from flask import Flask, render_template, request, redirect, url_for
import os

# Creiamo l'applicazione Flask
app = Flask(__name__)

# Lista in memoria per salvare i task
todos = []


# Route principale: mostra la pagina con la lista dei task
@app.route("/")
def index():
    return render_template("index.html", todos=todos)


# Route per aggiungere un nuovo task
@app.route("/add", methods=["POST"])
def add():
    # Prendiamo il testo del task dalla form HTML
    todo = request.form.get("todo")
    # Aggiungiamo il task solo se non è vuoto
    if todo:
        todos.append(todo)
    return redirect(url_for("index"))


# Route per eliminare un task tramite il suo indice
@app.route("/delete/<int:index>")
def delete(index):
    # Controlliamo che l'indice sia valido prima di eliminare
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for("index"))


#Leggiamo la variabile d'ambiente FLASK_ENV per la modalità debug
debug_mode = os.environ.get('FLASK_ENV') == 'development'


# Avviamo il server sulla porta 5000
if __name__ == "__main__":
    # nosec B104 - binding intenzionale per Docker
    app.run(host="0.0.0.0", port=5000, debug= debug_mode)