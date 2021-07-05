def inverter(s):
    return ' '.join(reversed(s.split()))

print(inverter('estou testando'))
print(inverter('novo teste de strings'))

def inversor_palavras(s):
    comprimento = len(s) 
    espacos = [' ']
    palavras = []
    i = 0 # 

    while i < comprimento:
        if s[i] not in espacos:
            inicio_palavra = i
            while i < comprimento and s[i] not in espacos: 
                i += 1
            palavras.append(s[inicio_palavra:i])
        i += 1
    return ''.join(reversed(s))

print(inversor_palavras('string de teste'))
print(inversor_palavras('Socorram-me, subi no ônibus em Marrocos'))