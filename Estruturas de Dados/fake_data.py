# Gerando Dados Falsos em Python
from faker import Faker 
fake_data = Faker()

# Criando nomes Falsos
name = fake_data.name()
print(name)

# Criando endereços Falsos
address = fake_data.address()
print(address)

# Criando email Falsos
email = fake_data.email()
print(email)
print('-'*30)

# Criando um Profile Falso
profile = fake_data.simple_profile()
for k, v in profile.items():
	print('{}: {}'.format(k,v))
print('-'*30)

# Gerando um Conjunto de Dados Maior
for _ in range(0,15):
	print(fake_data.name())

# Função para preencher uma lista com dados
def create_names_list(qty):
	names = []
	for _ in range(0,qty):
		names.append(fake_data.name())
	return names

lista = create_names_list(5)
print(lista)

# Utilizando o objeto Pessoa com nome, endereço, etc
class Pessoa:
	def __init__(self, nome, endereco, email):
		self.name = name 
		self.address = address 
		self.email = email 

	def __repr__(self):
		return 'nome: {}, endereco: {}, email: {}'.format(self.name, self.address, self.email)

# Criando uma Instância
pessoa = Pessoa(fake_data.name(), fake_data.address(), fake_data.email())
print(pessoa)

# Gerando uma Lista de do objeto classe Pessoa com fake data
lista_pessoas = []
for i in range(10):
	lista_pessoas.append(Pessoa(fake_data.name(), fake_data.address(), fake_data.safe_email()))
for x in lista_pessoas:
	print(x)

# Escrevendo dados falsos em um arquivo CSV
import csv 
with open('fake_data.csv', 'w', newline='') as csvfile:
	csv_fake_data = csv.writer(csvfile)
	for i in create_names_list(10):
		csv_fake_data.writerow([i])