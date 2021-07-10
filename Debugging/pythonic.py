livro = {"título":"Brave New World","autor":"Aldous Huxley"}
book = {"título":"1984"}

# Non-Pythonic
if "título" in livro and "autor" in livro:
    print("Título do livro: {título}, Autor: {autor}".format(**livro))
else:
    print("Faltando chaves")

# Pythonic
try:
    print("Título do livro: {título}, Autor: {autor}".format(**book))
except KeyError as e:
    print("Faltanto chave: {}".format(e))	

números = [1,2,3,4,5]
numbers = [1,2,3,4,5,6]

# Non-Pythonic
if len(números) >= 6:
    print(números[5])
else:
    print("Índice não existe na lista")

# Pythonic
try:
    print(numbers[5])
except IndexError:
    print('Índice não existe na lista')