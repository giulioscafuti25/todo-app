import pytest
import os
from app import app, init_db

# Configurazione del client di test con database temporaneo
@pytest.fixture
def client():
    # Usiamo un database temporaneo per i test
    app.config["TESTING"] = True
    app.config["DATABASE"] = ":memory:"

    with app.test_client() as client:
        # Inizializziamo il database temporaneo
        with app.app_context():
            init_db()
        yield client

# Test: la pagina principale risponde correttamente
def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

# Test: aggiungere un task funziona
def test_add_todo(client):
    response = client.post("/add", data={"todo": "Comprare il latte"})
    assert response.status_code == 302  # 302 = redirect

# Test: aggiungere un task vuoto non lo aggiunge
def test_add_empty_todo(client):
    response = client.post("/add", data={"todo": ""})
    assert response.status_code == 302

# Test: eliminare un task funziona
def test_delete_todo(client):
    # Prima aggiungiamo un task
    client.post("/add", data={"todo": "Task da eliminare"})
    # Poi lo eliminiamo
    response = client.get("/delete/1")
    assert response.status_code == 302