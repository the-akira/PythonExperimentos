import datetime

# Classe que define um Trabalhador
class Trabalhador:	

    n_de_trabalhadores = 0
    aumento = 1.04

    def __init__(self, nome, sobrenome, pagamento):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.pagamento = pagamento 
        self.email = f'{nome}{sobrenome}@google.com'

        Trabalhador.n_de_trabalhadores += 1

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def aplicar_aumento(self):
        self.pagamento = int(self.pagamento * self.aumento)

# Classe que define um Desenvolvedor (filha de Trabalhador)
class Desenvolvedor(Trabalhador):

    aumento = 1.10

    def __init__(self, nome, sobrenome, pagamento, prog_lang):
        super().__init__(nome, sobrenome, pagamento)
        self.prog_lang = prog_lang 

# Classe que define um Gerente (filha de Trabalhador)
class Gerente(Trabalhador):

    def __init__(self, nome, sobrenome, pagamento, trabalhadores=None):
        super().__init__(nome, sobrenome, pagamento)
        if trabalhadores is None:
            self.trabalhadores = []
        else:
            self.trabalhadores = trabalhadores

    def adicionar_trabalhador(self, trab):
        if trab not in self.trabalhadores:
            self.trabalhadores.append(trab)

    def remover_trabalhador(self, trab):
        if trab in self.trabalhadores:
            self.trabalhadores.remove(trab)

    def imprimir_trabalhadores(self):
        for trab in self.trabalhadores:
            print('-->', trab.nome_completo())

d1 = Desenvolvedor('Gabriel','Felippe',5000,'Python')
d2 = Desenvolvedor('Rafael','Marx',3000,'Java')
g1 = Gerente('Miguel','Felippe',2222,[d1])
g2 = Gerente('Miguel','Felippe',2222,[d2])

help(Desenvolvedor)
print(d1.email)
print(d1.prog_lang)
print(d2.email)
print(d2.prog_lang)
print(d1.pagamento)
d1.aplicar_aumento()
print(d1.pagamento)

g1.imprimir_trabalhadores()
g2.imprimir_trabalhadores()

print(isinstance(g1, Trabalhador))
print(isinstance(g1, Desenvolvedor))
print(issubclass(Gerente, Trabalhador))
print(issubclass(Desenvolvedor, Trabalhador))