# Criando classes em Python

# Sintaxe de alto nível
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p1 = Pessoa('Rafael')
print(p1.nome)
print(type(p1))
print(type(Pessoa))

# Sintaxe usando a função type()
def pessoa_init(self, nome):
    self.nome = nome

def dizer_nome(self):
    print(f'Meu nome é {self.nome}')

pessoa = type('Pessoa', (), {'__init__': pessoa_init, 'dizer_nome': dizer_nome})

print(pessoa.__name__)
p2 = pessoa('Gabriel')
print(p2.nome)
print(type(p2))
print(type(pessoa))
p2.dizer_nome()