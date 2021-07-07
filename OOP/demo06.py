class Trabalhador:
    pass

t1 = Trabalhador()
t2 = Trabalhador()

print(t1)
print(t2)

t1.nome = 'Gabriel'
t1.sobrenome = 'Felippe'
t1.email = 'gabriel@felippe.com'
t1.idade = 30

t2.nome = 'Rafael'
t2.sobrenome = 'Marx'
t2.email = 'rafael@marx.com'
t2.idade = 40

print(t1.email)
print(t2.email)