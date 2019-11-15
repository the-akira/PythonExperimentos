n1 = 123
n2 = -123
n3 = 120
n4 = 166
n5 = 1534236469
n6 = -2147483412

def inverter_int(n):
    if n == 0:
        return 0
    if n > 0:
        return int(''.join(reversed(str(n))))
    if n <= 0:
        return -1 * int(str(n*-1)[::-1])

# Trata overflow
def reverse_int(x):
    neg = False
    if x < 0:
        neg = True
        x = x * -1
    s = str(x)[::-1]
    n = int(s)
    if neg:
        n = n * -1
    if(abs(n) > (2 ** 31 - 1)):
        return 0
    return n

print(reverse_int(n5))
print(inverter_int(n5))