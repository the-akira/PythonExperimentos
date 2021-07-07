from PIL import Image
import os

dim_300 = (300, 300)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        # Separa o nome do arquivo e a extensão
        fn, fext = os.path.splitext(f) 
        i.thumbnail(dim_300)
        i.save('300/{}_300.png'.format(fn, fext))