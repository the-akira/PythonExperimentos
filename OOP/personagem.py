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
	print(f'Nome: {p5.nome}, Idade: {p5.idade}, Vida: {p5.vida}')

# p1 = Personagem() # Instanciamos um objeto do tipo Personagem
# p2 = Personagem() # Instanciamos outro objeto do tipo Personagem
# print(p1.nome, p1.idade, p1.vida, id(p1))
# print(p2.nome, p2.idade, p2.vida, id(p2))

# p1.nome = 'Mario'
# p1.idade = 35
# p1.vida = 3

# print(p1.nome, p1.idade, p1.vida)
# print(p2.nome, p2.idade, p2.vida)
# nome = p1.nome
# print(nome)

# expressao = f'Meu nome é {p1.nome} e eu possuo {p1.vida} ponto(s) de vida'
# print(expressao)

# p3 = Personagem()
# p3.nome = 'Arthas'
# p3.idade = 60
# p3.vida = 150

# p5 = Personagem('Samus', 30, 100)
# print(p5.nome, p5.idade, p5.vida)
# p5.upgrade_vida()
# print(p5.vida)

# imprimir_personagem(p5)

# print(str(p5))
# print(p5)

p6 = Mago('Gandalf', 1000, 1000)
print(p6)
p6.conjurar_magia()

print(isinstance(p6, Mago))
print(isinstance(p6, Personagem))

p6.upgrade_vida()

print(p6)

class Objeto(object):
    def __init__(self):
        self.x = 1    # Permitido o acesso direto
        self._x = 1   # Deve ser considerado privado
        self.__x = 1  # Considerado privado

obj = Objeto()
print(obj.x)
print(obj._x)
print(obj._Objeto__x)

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
