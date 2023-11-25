from fastapi import FastAPI

# Criar instância do FastAPI
app = FastAPI()

# Criar rota principal
@app.get("/")   # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo"}