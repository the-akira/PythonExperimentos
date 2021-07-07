class Carro:
    # Variáveis de classe
    rodas = 4
    # Método Construtor
    def __init__(self):
        self.kilometragem = 10
        self.fabricante = 'gurgel'

# Cria duas instâncias de carro
c1 = Carro()
c2 = Carro()

# Imprime os atributos do carro1 (c1)
print(c1.rodas, c1.kilometragem, c1.fabricante)