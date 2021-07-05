import time

cache = {}

def calculos(num):
    if num in cache:
        return cache[num]
    print(f'Computando {num}...')
    time.sleep(0.8)
    result = num * num
    cache[num] = result
    return result 

for i in range(15):
    calculos(i)

for i in range(15):
    print(calculos(i))