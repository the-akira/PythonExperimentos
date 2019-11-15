class Acumulador():
	def __init__(self,valor_inicial):
		self.estado_inicial = valor_inicial

	def get_proximo_valor(self,state,np):
		return (state,np,state+np)

a = Acumulador(1)
b = Acumulador(2)
print(a)
print(a.get_proximo_valor)
print(b)
print(b.get_proximo_valor)
