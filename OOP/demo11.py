class Trabalhador:	

    n_de_trabalhadores = 0
    aumento = 1.04

    def __init__(self, nome, sobrenome, pagamento):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.pagamento = pagamento 
        self.email = f'{nome}{sobrenome}@gmail.com'

        Trabalhador.n_de_trabalhadores += 1

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def aplicar_aumento(self):
        self.pagamento = int(self.pagamento * self.aumento)

    def __repr__(self):
        return f"Trabalhador('{self.nome}','{self.sobrenome}',{self.pagamento})"

    def __str__(self):
        return f'{self.nome_completo()} - {self.email}'

    def __add__(self, other):
        return self.pagamento + other.pagamento

    def __len__(self):
        return len(self.nome_completo())

t1 = Trabalhador('Gabriel','Felippe',5000)
t2 = Trabalhador('Rafael','Marx',3000)
print(t1)
print(str(t1))
print(repr(t1))
print(t1+t2)
print(len(t1))