import re

# Textos para buscar
texto = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

mat
pat
rat
bat
'''
sentença = 'Iniciar uma sentença e então finalizá-la'

# Raw String
print(r'\tTab')

# String Comum
print('\tTab')

# Padrões
pattern = re.compile(r'iniciar', re.I) # Palavra iniciar (Ignore case)
telefone = re.compile(r'[89]00[-.*]\d\d\d[-.*]\d\d\d') # Padrão para telefones 
pattern = re.compile(r'[1-5]') # Números entre 1-5
pattern = re.compile(r'[^a-zA-Z]') # Negação de letras a-z e A-Z
pattern = re.compile(r'[^b]at') # Negação do b
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # Outro padrão para telefones
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') # Padrão para buscar Mr. Mr Ms Mrs.

# Correspondências
matches = pattern.search(sentença)
matches = pattern.match(sentença)
matches = pattern.finditer(texto)
matches = pattern.findall(texto)

for match in matches:
    print(match)

# Abrindo um Arquivo
with open('dados.txt', 'r') as f:
    contents = f.read()
    matches = telefone.finditer(contents)
    for match in matches:
        print(match)