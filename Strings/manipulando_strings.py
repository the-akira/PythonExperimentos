from datetime import datetime

first_name = "Gabriel"
last_name = "Felippe"

sentenca_1 = "Meu nome é {} {}".format(first_name, last_name)

sentenca_2 = f'Meu nome e {first_name.upper()} {last_name.lower()}'

print(sentenca_2)

pessoa = {'nome': 'Pedro', 'idade': 22}

sentenca_3 = 'Meu nome é {} e eu tenho {} anos de idade'.format(pessoa['nome'], pessoa['idade'])

sentenca_4 = f'Meu nome é {pessoa["nome"]} e eu tenho {pessoa["idade"]} anos de idade'

print(sentenca_4)

calculo = f'4 vezes 11 é igual a {4 * 11}'

print(calculo)

for n in range(1,11):
	sentenca_5 = f'O Valor é {n:02}'
	print(sentenca_5)

pi = 3.14159265

sentenca_6 = f'Pi é igual a {pi:.7f}'

print(sentenca_6)

nascimento = datetime(1990, 5, 7)

sentenca_7 = f'O Nascimento é no dia {nascimento:%B %d, %Y}'

print(sentenca_7)