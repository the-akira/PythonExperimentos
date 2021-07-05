class Acumulador():
    def __init__(self,valor_inicial):
        self.estado_inicial = valor_inicial

    def get_proximo_valor(self,state,np):
        return (state,np,state+np)

    def __str__(self):
        return f'Acumulador({self.estado_inicial})'

a = Acumulador(1)
b = Acumulador(2)
print(a)
print(a.get_proximo_valor(1,2))
print(b)
print(b.get_proximo_valor(2,5))
print(b.get_proximo_valor(5,10))
