a = 5
b = 6

# Somar a + b
print(a+b)

# Somar a + b através do método __add__
print(int.__add__(a,b))
# Subtrair a - b através do método __sub__
print(int.__sub__(a,b))
# Multiplicar a * b através do método __mul__
print(int.__mul__(a,b))
# Verificar os atributos e métodos de int
print(dir(int))