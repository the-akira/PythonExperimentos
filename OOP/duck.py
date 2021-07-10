"""
Duck Typing
É um termo usado em linguagens dinâmicas que não possuem tipagem forte.
A ideia é que você não precisa de um tipo para invocar um método 
existente em um objeto, se um método for definido nele, você pode invocá-lo.
O nome vem da frase "Se parece um pato e grasna como um pato, então é um pato".
"""

"""
Neste caso, chamamos o método len() para obter o valor de retorno do método __len__. 
Aqui, o método __len__ define a propriedade da classe SpecialString.

O tipo do objeto em si não é significativo, 
pois não declaramos o argumento em protótipos de método. 
Isso significa que os compiladores não podem fazer verificação de tipo. 
Portanto, o que realmente importa é se o objeto possui atributos particulares 
em tempo de execução. Duck typing é, portanto, implementada por linguagens dinâmicas
"""

class SpecialString:
    def __len__(self):
        return 21

string = SpecialString()
print(len(string))
print(string.__len__())

"""
Este é um exemplo simples em Python 3 que demonstra como qualquer 
objeto pode ser usado em qualquer contexto, 
até que seja usado de uma forma não compatível.
"""

class Pato:
    def nadar(self):
        print('Pato está nadando')

    def voar(self):
        print('Pato está voando')

class Avião:
    def voar(self):
        print('Avião está voando')

class Baleia:
    def nadar(self):
        print('Baleia está nadando')

for animal in (Pato(), Baleia()):
    try:
        animal.nadar()
        animal.voar()
    except AttributeError as e:
        print(f'Erro: {e}')

avião = Avião()
avião.voar()

def nadar_voar(objeto):
    if isinstance(objeto, Pato):
        objeto.voar()
        objeto.nadar()
        print('Provavelmente é um pato')
    else:
        print('Provavelmente não é um pato')

def nadar_e_voar(objeto):
    try:
        objeto.voar()
        objeto.nadar()
    except AttributeError as e:
        print('Provavelmente não é um pato')

pato = Pato()
baleia = Baleia()

nadar_voar(pato)
nadar_voar(baleia)
nadar_e_voar(pato)
nadar_e_voar(baleia)