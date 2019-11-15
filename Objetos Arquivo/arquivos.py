# Objeto Arquivos

# f = open('teste.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()

with open('teste.txt', 'r') as f:
	# conteudo = f.read()
	content = f.readlines()
	# print(conteudo)
	print(content)