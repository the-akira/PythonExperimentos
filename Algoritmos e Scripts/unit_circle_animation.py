from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from celluloid import Camera
import numpy as np

float_range = np.arange(0.0, 30.0, 0.3).tolist()
x = np.linspace(0, 2*np.pi, 200)

fig = plt.figure(figsize=(10,10), dpi=80, facecolor='w', edgecolor='k')
camera = Camera(fig)
plt.grid()

red = mpatches.Patch(color='red', label='seno')
blue = mpatches.Patch(color='blue', label='cosseno')

for angulo in float_range:
    plt.plot(np.cos(x), np.sin(x), color='k', linewidth=3)
    plt.plot([-1.1,1.1], [0,0], '--', color='gray', linewidth=4)
    plt.plot([0,0], [-1.1,1.1], '--', color='gray', linewidth=4)

    plt.plot([0,np.cos(angulo)],[0,np.sin(angulo)], 'g', linewidth=3)
    plt.plot(np.cos(angulo),np.sin(angulo),'ko')

    plt.plot([0,np.cos(angulo)],[0,0],'b', linewidth=3)
    plt.plot([np.cos(angulo), np.cos(angulo)], [0, np.sin(angulo)], 'r', 
	    linewidth=3)
    camera.snap()

fig.suptitle('Unit Circle in Python', fontsize=25)
plt.legend(handles=[red,blue], fontsize=15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
animation = camera.animate()
animation.save('animation.gif')