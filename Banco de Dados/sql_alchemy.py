from sqlalchemy import create_engine, Column, Integer, String, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
	__tablename__ = 'person'

	id = Column('id', Integer, primary_key=True)
	username = Column('username', String, unique=True)

#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///users.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
# user = User()
# user.id = 0
# user.username = 'akira'

# session.add(user)
# session.commit()

users = session.query(User).all()
for user in users:
	print(user.username, user.id)

session.close()

