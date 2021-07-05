"""
Nome, Raio, Densidade, Distância do Sol
Raio no equador em kilometros
Densidade média em g/cm³
Distância do Sol (média) em Unidades Astronômica
1 Unidade Astronômica = Distância média da Terra com o Sol
"""

planetas = [
    ("Mercúrio", 2440, 5.43, 0.395),
    ("Vênus", 6052, 5.24, 0.723),
    ("Terra", 6378, 5.52, 1.000),
    ("Marte", 3396, 3.93, 1.53),
    ("Júpiter", 71492, 1.33, 5.210),
    ("Saturno", 60268, 0.69, 9.551),
    ("Uranu", 25559, 1.27, 19.213),
    ("Netuno", 24764, 1.64, 30.070),
]

nome = lambda planeta: planeta[0]
planetas.sort(key=nome, reverse=False)
print(f'Planetas ordenados por nome (asc): {planetas}')

tamanho = lambda planeta: planeta[1]
planetas.sort(key=tamanho, reverse=True)
print(f'Planetas ordenados por tamanho (desc): {planetas}')

densidade = lambda planeta: planeta[2]
planetas.sort(key=densidade, reverse=True)
print(f'Planetas ordenados por densidade (desc): {planetas}')

distancia = lambda planeta: planeta[3]
planetas.sort(key=distancia, reverse=True)
print(f'Planetas ordenados por distância (desc): {planetas}')