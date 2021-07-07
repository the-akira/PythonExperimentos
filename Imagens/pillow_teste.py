from PIL import Image
import os

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        # Separa o nome do arquivo e a extensão
        fn, fext = os.path.splitext(f) 
        i.save('png/{}.png'.format(fn))