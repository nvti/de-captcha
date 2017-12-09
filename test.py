from PIL import Image
import pytesseract
import argparse
import cv2
import os

image = cv2.imread("example_01.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
print(filename)

image_gray = Image.open(filename)

text = pytesseract.image_to_string(image_gray)

print(text)
