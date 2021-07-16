import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(height, width, x=-0.5, y=0, zoom=1, max_iterations=100):
    # Para facilitar a navegação, calculamos esses valores
    x_width = 1.5
    y_height = 1.5*height/width
    x_from = x - x_width/zoom
    x_to = x + x_width/zoom
    y_from = y - y_height/zoom
    y_to = y + y_height/zoom

    # Aqui o algoritmo real começa
    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    c = x + 1j * y

    # Inicializar z para zero
    z = np.zeros(c.shape, dtype=np.complex128)
    # Para acompanhar em qual iteração o ponto divergiu
    div_time = np.zeros(z.shape, dtype=int)
    # Para manter o controle sobre quais pontos não convergiram até agora
    m = np.full(c.shape, True, dtype=bool)

    for i in range(max_iterations):
        z[m] = z[m]**2 + c[m]

        diverged = np.greater(np.abs(z), 2, out=np.full(c.shape, False), where=m) # Find diverging

        div_time[diverged] = i   # definir o valor do número de iteração divergente
        m[np.abs(z) > 2] = False # para lembrar quais divergiram
    return div_time

# Imagem padrão do conjunto Mandelbrot
plt.imshow(mandelbrot(1200, 1400), cmap='magma')
plt.axis('off')
plt.show()