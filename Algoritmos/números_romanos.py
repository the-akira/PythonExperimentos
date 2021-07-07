from collections import OrderedDict

def romanos(num):
    """
    Função que converte números arábicos para romanos
    """
    romano = OrderedDict()
    romano[1000] = "M"
    romano[900] = "CM"
    romano[500] = "D"
    romano[400] = "CD"
    romano[100] = "C"
    romano[90] = "XC"
    romano[50] = "L"
    romano[40] = "XL"
    romano[10] = "X"
    romano[9] = "IX"
    romano[5] = "V"
    romano[4] = "IV"
    romano[1] = "I"

    def número_romano(num):
        for r in romano.keys():
            x, y = divmod(num, r)
            yield romano[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([n for n in número_romano(num)])

print(romanos(1))
print(romanos(50))
print(romanos(3))
print(romanos(7))