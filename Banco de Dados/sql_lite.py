import sqlite3
from pessoa import Pessoa 

conn = sqlite3.connect('pessoa.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE Pessoa (nome text, sobrenome text, idade integer)""")

def insert_pessoa(pessoa):
    with conn:
        cursor.execute("INSERT INTO Pessoa VALUES (:nome, :sobrenome, :idade)", {'nome': pessoa.nome, 'sobrenome': pessoa.sobrenome, 'idade': pessoa.idade})

def get_pessoa_por_sobrenome(sobrenome):
    cursor.execute("SELECT * FROM Pessoa WHERE sobrenome=:sobrenome", {'sobrenome': sobrenome})
    return cursor.fetchall()

def update_idade(pessoa, idade):
    with conn:
        cursor.execute("""UPDATE Pessoa SET idade = :idade WHERE nome = :nome AND sobrenome = :sobrenome""", {'nome': pessoa.nome, 'sobrenome': pessoa.sobrenome, 'idade': idade})

def remove_pessoa(pessoa):
    with conn:
        cursor.execute("DELETE from Pessoa WHERE nome = :nome AND sobrenome = :sobrenome", {'nome': pessoa.nome, 'sobrenome': pessoa.sobrenome})

pessoa = Pessoa('Gabriel', 'Felippe', 18)
persona = Pessoa('Rafael', 'Miguel', 20)
print(pessoa.nome)
print(pessoa.sobrenome)
print(pessoa.idade)

cursor.execute("INSERT INTO Pessoa VALUES (?, ?, ?)", (pessoa.nome, pessoa.sobrenome, pessoa.idade))
conn.commit()

cursor.execute("INSERT INTO Pessoa VALUES (:nome, :sobrenome, :idade)", {'nome': persona.nome, 'sobrenome': persona.sobrenome, 'idade': persona.idade})
conn.commit()

cursor.execute("SELECT * FROM Pessoa WHERE sobrenome=?", ('Felippe',))
print(cursor.fetchall())

cursor.execute("SELECT * FROM Pessoa WHERE sobrenome=:sobrenome", {'sobrenome': 'Miguel'})
print(cursor.fetchall())

insert_pessoa(pessoa)
insert_pessoa(persona)
update_idade(persona, 25)
remove_pessoa(pessoa)
pessoas = get_pessoa_por_sobrenome('Miguel')
print(pessoas)
conn.close()