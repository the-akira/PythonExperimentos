import decimal

def formula_fib_with_decimal(n):
    decimal.getcontext().prec = 10000
    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)
    a = ((phi ** n) - ((-phi) ** -n)) / root_5
    return round(a)

print(formula_fib_with_decimal(8))
print(formula_fib_with_decimal(15))