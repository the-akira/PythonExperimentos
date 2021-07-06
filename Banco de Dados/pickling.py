import pickle

class Animal:
    def __init__(self, nome, espécie):
        self.nome = nome 
        self.espécie = espécie 

    def __repr__(self):
        return f'{self.nome} é um {self.espécie}'

    def fazer_som(self, som):
        print(f'esse animal diz {som}')

class Gato(Animal):
    def __init__(self, nome, raça, brinquedo):
        super().__init__(nome, espécie='Gato')
        self.raça = raça 
        self.brinquedo = brinquedo 

    def brincar(self):
        print(f'{self.nome} brinca com {self.brinquedo}')

blue = Gato('Blue', 'Siamês', 'Cordinha')
brown = Gato('Brown', 'Persa', 'Peixinho')

with open('animais.pkl', 'wb') as file:
    pickle.dump(blue, file)
    pickle.dump(brown, file)

with open('animais.pkl', 'rb') as file: 
    blue = pickle.load(file)
    print(blue)
    blue.brincar()