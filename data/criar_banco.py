# criar_banco.py
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Entidade(Base):
    __tablename__ = 'entidades'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cnpj = Column(String)
    banco = Column(String)

engine = create_engine('sqlite:///data/banco.db')
Base.metadata.create_all(engine)

print("Banco de dados criado com sucesso em: data/banco.db")

