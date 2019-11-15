# 1. Invertendo uma String
nome = 'Heimdall'
nome_inverso = nome[::-1]
print(nome_inverso)

# 2. Utilizando Title Case (Primeiras letras maiúsculas)
frase = 'The most beautiful experience we can have is the mysterious'
nova_frase = frase.title()
print(nova_frase)

# 3. Buscando Elementos únicos em uma String
minha_string = 'aaabcwwwwwqqqqxxxx112'
temp_set = set(minha_string)
nova_string = ''.join(temp_set)
print(nova_string)

# 4. Checando se uma determinada string é palíndrome ou não
palavra = 'abcba'
if palavra == palavra[::-1]:
	print('palindrome')
else:
	print('not palindrome')

# 5. Descubra se duas Strings são Anagramas
from collections import Counter

str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, cnt_3  = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print('1 and 2 anagram')
if cnt_1 == cnt_3:
	print('1 and 3 anagram')

# 6. Amostragem de dados de uma Lista
import secrets # imports secure module.
secure_random = secrets.SystemRandom() # creates a secure random object.
my_list = ['a','b','c','d','e']
num_samples = 2
samples = secure_random.sample(my_list, num_samples)
print(samples)

# 7. Digitalizar: Converter um inteiro em uma lista de dígitos
num = 12345678954655
list_of_digits = list(map(int, str(num)))
print(list_of_digits)

# 8. Verificando Exclusividade (elementos da lista são únicos ou não)
def unique(l):
    if len(l)==len(set(l)):
        print("All elements are unique")
    else:
        print("List has duplicates")

unique([1,2,3,4,5,6])
unique([1,1,2,3])
