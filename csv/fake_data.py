from faker import Faker
import csv 

# Gerando Dados Falsos em Python com a biblioteca Faker
# Primeiramente instanciamos Faker
fake_data = Faker()

# Criando um nome falso
nome = fake_data.name()
print(nome)

# Criando um endereço falso
endereço = fake_data.address()
print(endereço)

# Criando um email falso
email = fake_data.email()
print(email)
print('-'*30)

# Criando um perfil falso
perfil = fake_data.simple_profile()
for chave, valor in perfil.items():
    print('{}: {}'.format(chave,valor))
print('-'*30)

# Gerando 10 nomes falsos
for _ in range(0,10):
    print(fake_data.name())

# Definimos uma função para preencher uma 
# Lista com nomes falsos gerados
def gerar_lista_nomes(quantidade):
    nomes = []
    for _ in range(0,quantidade):
        nomes.append(fake_data.name())
    return nomes

nomes = gerar_lista_nomes(5)
print(nomes)

# Definindo uma classe Pessoa
class Pessoa:
    def __init__(self, nome, endereço, email):
        self.nome = nome 
        self.endereço = endereço 
        self.email = email 

    def __repr__(self):
        return 'Nome: {}, Endereço: {}, Email: {}'.format(self.nome, self.endereço, self.email)

# Criando uma instância de Pessoa
pessoa = Pessoa(fake_data.name(), fake_data.address(), fake_data.email())
print(pessoa)

# Gerando uma Lista de objetos Pessoa
pessoas = []
for i in range(10):
    pessoas.append(Pessoa(fake_data.name(), fake_data.address(), fake_data.safe_email()))
for p in pessoas:
    print(p)

# Escrevendo dados falsos em um arquivo CSV
with open('dadosfalsos.csv', 'w', newline='') as csvfile:
    csv_fake_data = csv.writer(csvfile)
    for i in gerar_lista_nomes(10):
        csv_fake_data.writerow([i])