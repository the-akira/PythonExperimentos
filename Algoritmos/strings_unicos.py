"""
Dada uma string, são todos os carácteres únicos?
Deve nos retornar True ou False
Utilizar estruturas construídas em Python
"""

def único(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string)

print(f'cavalo = {único("cavalo")}')
print(f'cachorro = {único("cachorro")}')
print(f'queijo = {único("queijo")}')

def única(s):
    s = s.replace(' ','')
    caracteres = set()
    for letra in s:
        if letra in caracteres:
            return False
        else:
            caracteres.add(letra)
    return True

print(f'ijkl = {única("ijkl")}')
print(f'kiki = {única("kiki")}')
print(f'kacoe = {única("kacoe")}')