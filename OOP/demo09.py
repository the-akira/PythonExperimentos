import datetime

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

    @classmethod 
    def set_aumento(cls, amount):
        cls.aumento = amount 

    @classmethod 
    def from_string(cls, emp_str):
        nome, sobrenome, pagamento = emp_str.split('-')
        return cls(nome, sobrenome, pagamento)

    @staticmethod 
    def é_dia_de_trabalho(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False 
        return True

t1 = Trabalhador('Gabriel','Felippe',5000)
t2 = Trabalhador('Rafael','Marx',3000)

t = 'Samuel-Oliveira-7000'
t3 = Trabalhador.from_string(t)
print(t3.nome)
print(t3.sobrenome)

Trabalhador.set_aumento(1.05)

print(Trabalhador.aumento)
print(t1.aumento)
print(t2.aumento)

data = datetime.date(2017, 7, 17)
print(Trabalhador.é_dia_de_trabalho(data))