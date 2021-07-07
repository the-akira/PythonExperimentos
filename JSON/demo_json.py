import json 

class Cat:
    def __init__(self, nome, raça):
        self.nome = nome 
        self.raça = raça 

c = Cat('Charles', 'Persa')

j = json.dumps(c.__dict__, ensure_ascii=False)
print(j)