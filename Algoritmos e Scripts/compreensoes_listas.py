# Vamos cobrir alguns exemplos de compreensões de lista
# [ expressao for valor in colecao ]
# [ expressao for valor in colecao if <teste 1> and <teste 2> ]
# [ expressao for valor1 in colecao1 and valor2 in colecao2 ]

quadrados = [i**2 for i in range(10)]
print(quadrados)
print()

resto_5 = [x**2 % 5 for x in range(1,101)]
print(resto_5)
print()

resto_11 = [x**2 % 11 for x in range(1,101)]
print(resto_11)
print()

# Multiplicação escalar
vetor = [-2, -3, 1]
w = [4*x for x in vetor]
print(w)
print()

# Produto cartesiano
A = [1,2,3,7]
B = [2,4,6,8]

produto_cartesiano = [(a,b) for a in A for b in B]
print(produto_cartesiano)
