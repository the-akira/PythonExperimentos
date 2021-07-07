from collections import deque

k = 2 
x = [-1,-100,3,99]

def rotate(l, k):
    return l[-k:] + l[:-k]

def rotacao(l, k):
    return [l[(i - k) % len(l)] for i, x in enumerate(l)]

def rotation(l, k):
    d = deque(l)
    d.rotate(k)
    return list(d)

def rotacionar(l, k):
    while k != 0:
        l.insert(0, l.pop())
        k = k - 1 
    return l

print(rotate(x, k))
print(rotacao(x, k))
print(rotation(x, k))
print(rotacionar(x, k))