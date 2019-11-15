from PIL import Image, ImageFilter
import os

image1 = Image.open('2.jpg')
#image1.rotate(90).save('2_mod.jpg')
#image1.convert(mode='L').save('2_mod2.jpg')
image1.filter(ImageFilter.GaussianBlur(12)).save('3_mod.jpg')
