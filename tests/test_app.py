import pytest
from app import app

#Configurazione del client di test
@pytest.fixture
def client():
    #Mettiamo l'app in modalità test
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

#Test: la pagina principale risponde correttamente
def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

#Test: aggiungere un task funziona
def test_add_todo(client):
    response = client.post("/add", data={"todo":"Comprare il latte"})
    assert response.status_code == 302 #302 redirect

#Test: aggiungere un task vuoto non lo aggiunge
def test_add_empty_todo(client):
    response = client.post("/add", data={"todo": ""})
    assert response.status_code == 302

#Test: eliminare una task funziona
def test_delete_todo(client):
    #Prima aggiungiamo una task
    client.post("/add", data={"todo": "Task da eliminare"})
    #Poi la eliminiamo
    response = client.get("/delete/0")
    assert response.status_code == 302