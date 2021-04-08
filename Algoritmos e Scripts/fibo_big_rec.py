cache = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
}

def recursiveFib(n):
    if cache.get(n, None) is None:
        # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
        # F(2n-1) = F(n-1)^2 + F(n)^2
        # F(2n) = (2F(n-1) + F(n)) * F(n)
        if n % 2:
            f1 = recursiveFib((n - 1) / 2)
            f2 = recursiveFib((n + 1) / 2)
            cache[n] = f1 ** 2 + f2 ** 2
        else:
            f1 = recursiveFib(n / 2 - 1)
            f2 = recursiveFib(n / 2)
            cache[n] = (2 * f1 + f2) * f2

    return cache[n]


print(recursiveFib(1_000_000))
