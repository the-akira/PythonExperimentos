class Trabalhador:	

    n_de_trabalhadores = 0
    aumento = 1.04

    def __init__(self, nome, sobrenome, pagamento):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.pagamento = pagamento 
        self.email = nome + '.' + sobrenome + '@company.com'

        Trabalhador.n_de_trabalhadores += 1

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def aplicar_aumento(self):
        self.pagamento = int(self.pagamento * self.aumento)

t1 = Trabalhador('Gabriel','Felippe',5000)
t2 = Trabalhador('Rafael','Marx',3000)

print(t1.pagamento)
print(t1.aumento)
print(Trabalhador.aumento)
t1.aplicar_aumento()
print(t1.pagamento)
print(t1.__dict__)
print(Trabalhador.__dict__)
print(Trabalhador.n_de_trabalhadores)