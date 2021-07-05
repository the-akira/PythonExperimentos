import statistics

# Mapeando de Celsius para Fahrenheit
celsius = [
	('Berlin', 29), 
	('Cairo', 36), 
	('Buenos Aires', 19), 
	('Rio de Janeiro', 39), 
	('Tokyo', 27), 
	('New York', 28), 
	('Beijing', 32)
]
celsius_para_fahrenheit = lambda dados: (dados[0], (9/5)*dados[1] + 32)
print(list(map(celsius_para_fahrenheit,celsius)))

# Filtrando dados
dados_numericos = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados_numericos)
print(f'A média dos dados númericos é = {media}')
filter(lambda x: x > media, dados_numericos)
maiores_media = list(filter(lambda x: x > media, dados_numericos))
menores_media = list(filter(lambda x: x < media, dados_numericos))
print(f'Valores maiores que a media = {maiores_media}')
print(f'Valores menores que a media = {menores_media}')

# Removendo dados que estão faltando
paises = ['', 'Argentina', '', 'Nigeria', '', 'Colombia', '', 'China', '', 'India', '', 'Paquistao']
print(list(filter(None, paises))) 