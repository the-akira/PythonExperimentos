import matplotlib.pyplot as plt
import numpy as np
 
m = 600 # Largura
n = 395 # Altura
s = 2800 # Escala
c = -0.162 + 1.04j

x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))
Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))

C = np.full((n, m), c)
M = np.full((n, m), True)
N = np.zeros((n, m))

for i in range(70):
    Z[M] = Z[M] * Z[M] + C[M]
    M[np.abs(Z) > 2] = 0
    N[M] = i
 
fig = plt.figure()
fig.set_size_inches(m / 100, n / 100)
ax = fig.add_axes([0, 0, 1, 1])
plt.imshow(N, cmap='twilight_shifted')
plt.savefig('julia_set.png')