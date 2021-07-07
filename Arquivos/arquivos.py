# Objeto Arquivos

f = open('teste.txt', 'r')
print(f.name)
print(f.mode)
print(f.readline())
f.close()

with open('teste.txt', 'r') as f:
    conteúdo = f.read()
    print(conteúdo)