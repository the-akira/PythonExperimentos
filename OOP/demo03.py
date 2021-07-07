class Estudante:

    escola = 'Escola Politécnica'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def média(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, valor):
        self.m1 = valor

    @classmethod
    def info(cls):
        return cls.escola

    @staticmethod
    def imprimir_escola(cls):
        print(f'Escola que você estuda é {cls.escola}')

# Cria duas instâncias de estudantes
e1 = Estudante(6,3,10)
e2 = Estudante(3,10,7)
# Imprime a média do estudante1 (e1)
print(e1.média())
# Imprime a primeira nota do estudante1 (e1)
print(e1.get_m1())
# Imprime a média do estudante2 (e2)
print(e2.média())
# Obtém informações do estudante
print(Estudante.info())
print(e1.info())
# Imprime a escola do estudante1 (e1)
Estudante.imprimir_escola(e1)