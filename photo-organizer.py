import os
from PIL import Image
from datetime import datetime

#print("Hello World")


def photoShotingData(file):
    photo = Image.open(file)
    info = photo._getexif()
    if info == None:
        print('sim')
    else:
        print('nao')

    return info


print(photoShotingData('test1.jpg'))

'''
if 36867 in info:
    date = info[36867]
    date = datetime.strptime(date,'%Y:%m:%d %H:%M:%S')
  else:
    date = datetime.fromtimestamp(os.path.getmtime(file))
'''
