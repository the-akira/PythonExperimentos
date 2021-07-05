# Funções construídas Python
dec = 255
print(f'Versão decimal {dec}')
print(f'Versão binária {bin(dec)}')
print(f'Versão octal {oct(dec)}')
print(f'Versão hexadecimal {hex(dec)}')

print('-'*50)

def conversor(num, from_base, to_base):
    """
    Conversão de decimal para binário <> binário para decimal
    num -> número escolhido
    from_base -> base do número escolhido
    to_base -> base a ser convertido
    """
    to_num, power = 0, 0
    while num > 0:
        to_num += from_base ** power * (num % to_base)
        num //= to_base 
        power += 1
    return to_num

# Binário para decimal
print(f'11(bin) -> {conversor(11, 2, 10)}(dec)')
print(f'111(bin) -> {conversor(111, 2, 10)}(dec)')
# Decimal para binário
print(f'127(dec) -> {conversor(127, 10, 2)}(bin)')
print(f'13(dec) -> {conversor(13, 10, 2)}(bin)')

print('-'*50)

# F-Strings
num = 255
print(f'Decimal = {num:.2f}')
print(f'Hexadecimal = {num:x}')
print(f'Binário = {num:b}')
print(f'Octal = {num:o}')
print(f'Notação Científica = {num:e}')