from fastapi import FastAPI
from app.routes import router

# Criar instância do FastAPI
app = FastAPI()

app.include_router(router)
