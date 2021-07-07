from collections import Counter

s = 'abcd'
t = 'abcde'

def diferença(s, t):
    x = set(s)
    y = set(t)
    return max(y.difference(x))

def dif(s, t):
    return list(Counter(t) - Counter(s))[0]

print(diferença(s, t))
print(dif(s, t))