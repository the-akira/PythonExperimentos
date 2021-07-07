class Personagem:
    """
    A class Personagem representa as características de uma identidade personagem em um jogo
    """
    def __init__(self, nome, idade, vida):
        """
        Inicializa as propriedades de um personagem
        """
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def upgrade_vida(self):
        self.vida += 10

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'

class Mago(Personagem):
    def conjurar_magia(self):
        print(f'{self.nome} lança uma magia aleatória')

    def upgrade_vida(self):
        self.vida += 5

def imprimir_personagem(p):
    print(f'Nome: {p.nome}, Idade: {p.idade}, Vida: {p.vida}')

# Instanciamos dois objetos do tipo Personagem
p1 = Personagem('Mario', 35, 3) 
p2 = Personagem('Alucard', 37, 5)
print(p1.nome, p1.idade, p1.vida, id(p1))
print(p2.nome, p2.idade, p2.vida, id(p2))

expressão = f'Meu nome é {p1.nome} e eu possuo {p1.vida} ponto(s) de vida'
print(expressão)

# Instanciamos mais dois objetos do tipo Personagem
p3 = Personagem('Arthas', 60, 150)
p4 = Personagem('Samus', 30, 100)
print(p4.nome, p4.idade, p4.vida)
p4.upgrade_vida()
print(p4.vida)
imprimir_personagem(p4)
print(str(p4))
print(p4)

# Instanciamos mais um objeto do tipo Personagem
p5 = Mago('Gandalf', 1000, 1000)
print(p5)
p5.conjurar_magia()
print(isinstance(p5, Mago))
print(isinstance(p5, Personagem))
p5.upgrade_vida()
print(p5)

# Definimos uma classe Objeto de exemplo
class Objeto(object):
    def __init__(self):
        self.x = 1    # Permitido o acesso direto
        self._x = 1   # Deve ser considerado privado
        self.__x = 1  # Considerado privado

obj = Objeto()
print(obj.x)
print(obj._x)
print(obj._Objeto__x)

# Definimos uma classe Criatura de exemplo
class Criatura:
    def __init__(self, nome):
        self.nome = nome 

    def informacao(self):
        raise NotImplementedError("Subclasse deve Implementar o método Abstrato")

class Orc(Criatura):
    def informacao(self):
        return 'Criatura tribal shamânica misteriosa'

class Minotauro(Criatura):
    def informacao(self):
        return 'Criatura poderosa que vive nos labirintos'

criaturas = [Orc('Orc 1'), Orc('Orc 2'), Minotauro('Minotauro')]

for criatura in criaturas:
    print(f'Nome: {criatura.nome}, Informações: {criatura.informacao()}')