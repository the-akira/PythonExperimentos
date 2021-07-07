from hashlib import sha256

x = 5
y = 0 # Não sabemos o que y deve ser, ainda...

print(sha256(str(x*y).encode()).hexdigest())

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1

print(f'A solução é y = {y}')