import pytesseract
from PIL import Image
imag = Image.open('img.jpg')
vcode = pytesseract.image_to_string(imag)
print(vcode)