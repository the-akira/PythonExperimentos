from hashlib import sha256

x = 5
y = 0  # We don't know what y should be yet...

print(sha256(str(x*y).encode()).hexdigest())

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
	y += 1

print(f'The solution is y = {y}')