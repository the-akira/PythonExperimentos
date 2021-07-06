import pprint as pp

# Funções Lambda, também conhecidas como Funções Anônimas
# lambda argumento: expressão
add = lambda x: x + 3
print(add(3))

quadrado = lambda x: x * x 
print(quadrado(5))

nome_completo = lambda nome,sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo('Victor','Hugo'))

# Lambda como argumento em outras funções
# Um uso muito popular para as funções lambda é como argumento em funções filter ou sort
autores_scifi = [
    'Isaac Asimov',
    'Ray Bradbury',
    'Robert Heinlein',
    'Arthur C. Clarke',
    'Frank Herbert',
    'Orson Scott Card',
    'Douglas Adams',
    'H. G. Wells', 
    'Leigh Brackett'
]

# Ordenando autores em ordem alfabética
autores_scifi.sort(key=lambda nome: nome.split(' ')[0].lower())
print(autores_scifi)

# Ordenando alimentos por quantidade crescente
alimentos = [('ovos', 10),('pães', 5),('tomate', 6),('cenoura', 4),('maçã', 3)]
alimentos.sort(key = lambda x: x[1])
print(alimentos)

# Ordenando pokémons por tipo
pokédex = [
    {'nome':'pikachu','tipo':'elétrico'},
    {'nome':'charizard','tipo':'fogo'},
    {'nome':'bulbasaur','tipo':'planta'},
    {'nome':'squirtle','tipo':'aquatico'}
]
pokemon = sorted(pokédex, key=lambda x: x['tipo'])
pp.pprint(pokemon)

# Filtrando uma lista de inteiros usando lambda, selecionas apenas pares
lista = [1,2,3,4,5,6]
filtro = list(filter(lambda x: x%2 == 0,lista))
print(filtro)

# Selecionando apenas ímpares
impares = lambda x: x%2 == 1 
print(list(filter(impares,lista)))

# Usando map para elevar todos os valores ao quadrado
print(list(map(lambda x: x**2,lista)))

# Também podemos usar condicionais com lambda
comeca_com_G = lambda x: True if x.startswith('G') else False 
print(comeca_com_G('Gabriel'))
print(comeca_com_G('Felippe'))

# Selecionando a palavra que vem antes de uma palavra na sentença
palavra_antes = lambda s, w: s.split()[s.split().index(w)-1] if w in s else None 
sentenca = 'Rato Roeu Roupa Rei Roma'
print(palavra_antes(sentenca,'Roma'))

# Usando lambda para construir uma função que cria funções
def construcao_quadraticas(a, b, c):
    """Retorna a função f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c 

f = construcao_quadraticas(4,7,-6)
print(f(0))
print(f(3))