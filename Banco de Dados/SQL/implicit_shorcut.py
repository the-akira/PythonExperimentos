import sqlite3

pokemons = [
    ("Bulbasaur", "Grass"),
    ("Charmander", "Fire"),
    ("Squirtle", "Water"),
    ("Pikachu", "Electric")
]

con = sqlite3.connect(":memory:")

con.execute("create table pokemon(name, type)")

con.executemany("insert into pokemon(name, type) values (?, ?)", pokemons)

for row in con.execute("select name, type from pokemon"):
    print(row)

con.close()