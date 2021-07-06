def somar_tudo(*args):
    total = 0
    for num in args:
        total += num 
    return total

print(somar_tudo(2,3,4,6))
print(somar_tudo(2,3,4,6,5,5,5,1,2))
print(somar_tudo(2,3))