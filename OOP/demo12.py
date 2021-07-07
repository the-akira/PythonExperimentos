class Trabalhador:	

    n_de_trabalhadores = 0
    aumento = 1.04

    def __init__(self, nome, sobrenome, pagamento):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.pagamento = pagamento 

        Trabalhador.n_de_trabalhadores += 1

    @property	
    def email(self):
        return f'{self.nome}.{self.sobrenome}@email.com'

    @property	
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter 
    def nome_completo(self, name):
        nome, sobrenome = name.split(' ')
        self.nome = nome 
        self.sobrenome = sobrenome

    @nome_completo.deleter 
    def nome_completo(self):
        print('Nome removido!')
        self.nome = None
        self.sobrenome = None

t1 = Trabalhador('Gabriel','Felippe',5000)
t2 = Trabalhador('Rafael','Marx',3000)
t1.nome_completo = 'Rafael Felippe'
print(t1.nome)
print(t1.email)
print(t1.nome_completo)
del t1.nome_completo
print(t1.nome_completo)