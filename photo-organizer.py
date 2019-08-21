import os
from PIL import Image

#print("Hello World")

def photoShotingData(file):
  photo = Image.open(file)
  info = photo._getexif()
  return os.path.getsize(file)

print(photoShotingData('vitor.jpg'))