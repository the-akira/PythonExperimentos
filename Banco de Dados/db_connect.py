import sqlite3

def imprimir_db():
    try:
        result = cursor.execute("SELECT id, Nome, Sobrenome, Idade, Endereço, DataCadastro FROM Pessoas")
        for row in result:
            print(f"ID: {row[0]}")
            print(f"Nome: {row[1]}")
            print(f"Sobrenome: {row[2]}")
            print(f"Idade: {row[3]}")
            print(f"Endereço: {row[4]}")
            print(f"DataCadastro: {row[5]}")
    except sqlite3.OperationalError:
        print("A Tabela não existe")
    except:
        print("Não é possível recuperar os dados do banco de dados")
 
db_conn = sqlite3.connect('pessoas.db')
print("Banco de dados criado.")
cursor = db_conn.cursor()

try:
    db_conn.execute("CREATE TABLE Pessoas(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Nome TEXT NOT NULL, Sobrenome TEXT NOT NULL, Idade INT NOT NULL, Endereço TEXT, DataCadastro TEXT);")
    db_conn.commit()
    print("Tabela criada com sucesso")
except sqlite3.OperationalError:
    print("Tabela não pode ser criada")
 
db_conn.execute("INSERT INTO Pessoas (Nome, Sobrenome, Idade, Endereço, DataCadastro)"
                "VALUES ('Gabriel', 'Felippe', 30, 'Avenida Castelo 88', date('now'))")
db_conn.commit()
print("Pessoa inserida com sucesso")
imprimir_db()
db_conn.close()