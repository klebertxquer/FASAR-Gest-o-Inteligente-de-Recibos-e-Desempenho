from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Caminho do banco
DB_PATH = os.path.join("data", "banco.db")
engine = create_engine(f'sqlite:///{DB_PATH}', echo=False)

Base = declarative_base()

class Entidade(Base):
    __tablename__ = 'entidades'

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    nome = Column(String)
    documento = Column(String)
    banco = Column(String)
    agencia = Column(String)
    conta = Column(String)
    pix = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
