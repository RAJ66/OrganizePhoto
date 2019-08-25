import os
from PIL import Image
from datetime import datetime
import shutil
#
extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']


def folderPathFromPhotoDate(file):
    date = photoShotingData(file)
    return date.strftime('%Y')+'/'+date.strftime('%Y-%m-%d')


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


def movePhoto(file):
    newFolder = folderPathFromPhotoDate(file)
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)

    shutil.move(file, newFolder+'/'+file)
    print('||'+file+'||'+' Complete||')


def organize():
    photos = [
        filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extensions)
    ]
    for name in photos:
         movePhoto(name)

# execute
print(organize())




