from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Caminho do banco
caminho = os.path.join('data', 'banco.db')

# Cria a pasta se não existir
os.makedirs('data', exist_ok=True)

# Criação do engine
engine = create_engine(f'sqlite:///{caminho}')
Base = declarative_base()

# Modelo da tabela
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

# Cria as tabelas
Base.metadata.create_all(engine)

# Sessão
Session = sessionmaker(bind=engine)
session = Session()

# Dados de exemplo
exemplo = Entidade(
    tipo='Empresa',
    nome='FASAR HOLDING',
    documento='47.292.627/0001-00',
    banco='Caixa Econômica Federal',
    agencia='0352',
    conta='5772443832',
    pix='47.292.627/0001-00'
)

session.add(exemplo)
session.commit()
print(f"Banco criado com sucesso em: {caminho}")
