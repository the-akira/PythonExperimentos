# Python Funções Lambda
## Funções anônimas
## lambda argumentos: expressão
import pprint as pp

add3 = lambda x: x + 3
print(add3(3))

quadrado = lambda x: x * x 
print(quadrado(5))

nome_completo = lambda nome,sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo('Victor','Hugo'))

# Lambda como argumento em outras funções
## Um uso muito popular para as funções lambdas é como argumento dentro de funções filter ou sort

autores_scifi = ['Isaac Asimov','Ray Bradbury','Robert Heinlein','Arthur C. Clarke',
				'Frank Herbert','Orson Scott Card','Douglas Adams','H. G. Wells', 'Leigh Brackett']

autores_scifi.sort(key=lambda nome: nome.split(' ')[0].lower())
print(autores_scifi)

alimentos = [('ovos', 10),('pães', 5),('tomate', 6),('cenoura', 4),('maçã', 3)]
alimentos.sort(key = lambda x: x[1])
print(alimentos)

pokedex = [
	{'nome':'pikachu','tipo':'elétrico'},
	{'nome':'charizard','tipo':'fogo'},
	{'nome':'bulbasaur','tipo':'planta'},
	{'nome':'squirtle','tipo':'aquatico'}
]

pokemon = sorted(pokedex, key=lambda x: x['tipo'])
pp.pprint(pokemon)

# Filtrando uma lista de inteiros usando Lambda

l = [1,2,3,4,5,6]
filtro = list(filter(lambda x: x%2 == 0,l))
print(filtro)

impares = lambda x: x%2 == 1 
print(list(filter(impares,l)))

# Função Lambda em uma lista usando Map

print(list(map(lambda x: x ** 2,l)))

# Condicionais com Lambda
## lambda argumentos: a if expressao_booleana else b

comeca_com_G = lambda x: True if x.startswith('G') else False 
print(comeca_com_G('Gabriel'))
print(comeca_com_G('Felippe'))

palavra_antes = lambda s, w: s.split()[s.split().index(w)-1] if w in s else None 
sentenca = 'Rato Roeu Roupa Rei Roma'
print(palavra_antes(sentenca,'Roma'))

# Função que cria funções
def construcao_quadraticas(a, b, c):
	"""Retorna a função f(x) = ax^2 + bx + c"""
	return lambda x: a*x**2 + b*x + c 

f = construcao_quadraticas(4,7,-6)
print(f(0))
print(f(3))

