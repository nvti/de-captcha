import tesserocr
from PIL import Image

image = Image.open('text0_bolder.png')

text = tesserocr.image_to_text(image)  # print ocr text from image
print(text)
