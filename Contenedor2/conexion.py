from sqlalchemy import create_engine
from config import Config

def conectar():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    return engine