from sqlalchemy import create_engine

engine = create_engine('sqlite:///meubanco.db', echo = True, pool_size = 5)

# conn = create_engine("duckdb:///duck.db").connect()
#dialect+driver://username:password@host:port/database
#URI = "postgresql+pyodc://dbuser:kx%40jj5%2Fg@pghost10/appdb"
print ("Conexão com SQLite estabelecida.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key = True)
    nome = Column(String)
    idade = Column(Integer)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

#novo_usuario = Usuario(nome='João', idade = 28)
#session.add(novo_usuario)
#session.commit()
#print("Usuário inserido com sucesso")
#usuario = session.query(Usuario).filter_by(nome ="João").first()
#print(f"Usuário encontrado: {usuario.nome}, Idade; {usuario.idade}")

try:
    novo_usuario = Usuario(nome='Ana', idade = 24)
    session.add(novo_usuario)
    session.commit()
    print("Usuário inserido com sucesso")
except:
    session.rollback()
finally:
    session.close()