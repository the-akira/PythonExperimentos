from sqlalchemy import create_engine, Column, Integer, String, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Usuário(Base):
    __tablename__ = 'usuário'

    id = Column('id', Integer, primary_key=True)
    nome = Column('nome', String, unique=True)

engine = create_engine('sqlite:///usuários.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
user = Usuário()
user.id = 0
user.nome = 'akira'
session.add(user)
session.commit()

usuários = session.query(Usuário).all()
for usuário in usuários:
    print(f'Nome: {usuário.nome} | ID: {usuário.id}')

session.close()