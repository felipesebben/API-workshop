from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Configurar a conexão com o banco de dados
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Criar a engine de conexão
engine = create_engine(DATABASE_URL)

# Criar fábrica de sessões do SQLAlchemy que será usada para criar sessoẽs
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# Definir função geradora que fornecesse sessão de dados e garante o fechamento da sessão
def get_db():
    """
    Cria uma sessão de banco de dados para uso no decorrer da requisição.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
