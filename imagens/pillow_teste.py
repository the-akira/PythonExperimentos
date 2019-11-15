from PIL import Image
import os

#image1 = Image.open('1.jpg')
#image1.show()
#image1.save('illuminati.png')

for f in os.listdir('.'):
	if f.endswith('.jpg'):
		i = Image.open(f)
		fn, fext = os.path.splitext(f) # Separa o nome do arquivo e a extensão
		i.save('png/{}.png'.format(fn))