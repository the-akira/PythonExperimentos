from datetime import datetime

# Manipulando e Formatando Strings com format() e F-Strings

nome = "Gabriel"
sobrenome = "Felippe"

sentença1 = "Meu nome é {} {}".format(nome, sobrenome)
print(sentença1)

sentença2 = f'Meu nome e {nome.upper()} {sobrenome.lower()}'
print(sentença2)

pessoa = {'nome': 'Rafael', 'idade': 22}

sentença3 = 'Meu nome é {} e eu tenho {} anos de idade'.format(pessoa['nome'], pessoa['idade'])
print(sentença3)

sentença4 = f'Meu nome é {pessoa["nome"]} e eu tenho {pessoa["idade"]} anos de idade'
print(sentença4)

cálculo = f'4 vezes 11 é igual a {4 * 11}'
print(cálculo)

for n in range(1,11):
    sentença5 = f'O Valor é {n:02}'
    print(sentença5)

pi = 3.14159265

sentença6 = f'Pi é igual a {pi:.7f}'
print(sentença6)

nascimento = datetime(1990, 5, 7)

sentença7 = f'O Nascimento é no dia {nascimento:%B %d, %Y}'
print(sentença7)