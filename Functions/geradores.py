def números_ao_quadrado(números):
    resultado = []
    for n in números:
        resultado.append(n*n)
    return resultado

nums = números_ao_quadrado([1,2,3,4,5])
print(nums)

def gerador_quadrados(números):
    for n in números:
        yield(n*n)

nums = gerador_quadrados([1,2,3,4,5])
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

números = [x*x for x in [1,2,3,4,5]]
print(list(números))

for n in números:
    print(n)