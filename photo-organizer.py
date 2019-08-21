import os
from PIL import Image
from datetime import datetime
#7


def photoShotingData(file):
    photo = Image.open(file)
    info = photo._getexif()
    if info == None:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    else:
        if 36867 in info:
            date = info[36867]
            date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')

    return date


print(photoShotingData('test1.jpg'))
print(photoShotingData('vitor.jpg'))



