from PIL import Image
import pytesseract
import numpy as np

filename = 'text.png'
image = np.array(Image.open(filename))
text = pytesseract.image_to_string(image).strip()
print(text)