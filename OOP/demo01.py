# Define uma classe que representa um computador
class Computador:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram 

    def config(self):
        print(f'Configurações: {self.cpu} / {self.ram}')

# Cria duas instâncias de Computador
comp1 = Computador('i3','4')
comp2 = Computador('i5','16')

# Imprime o tipo
print(type(comp1))
# Chama o método config()
Computador.config(comp1)
comp2.config()

# Endereço em memória dos objetos
print(id(comp1)) 
print(id(comp2))