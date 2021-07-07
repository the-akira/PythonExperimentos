# Classe que define um Trabalhador
class Trabalhador:	
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.idade = idade 
        self.email = f'{nome}{sobrenome}@gmail.com'

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

# Cria duas instâncias de trabalhador
t1 = Trabalhador('Gabriel','Felippe',35)
t2 = Trabalhador('Rafael','Marx',25)

print(t1.nome_completo())
print(t1.email)
print(t2.nome_completo())
print(Trabalhador.nome_completo(t1))