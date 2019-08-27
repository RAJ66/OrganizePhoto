import os
from PIL import Image
from datetime import datetime
import shutil
# 5


class PhotoOrganizer:

    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']

    def folderPathFromPhotoDate(self,file):
        date = self.photoShotingData(file)
        return date.strftime('%Y')+'/'+date.strftime('%Y-%m-%d')

    def photoShotingData(self,file):
        photo = Image.open(file)
        info = photo._getexif()
        if info == None:
            date = datetime.fromtimestamp(os.path.getmtime(file))
        else:
            if 36867 in info:
                date = info[36867]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')

        return date

    def movePhoto(self,file):
        newFolder = self.folderPathFromPhotoDate(file)
        if not os.path.exists(newFolder):
            os.makedirs(newFolder)

        shutil.move(file, newFolder+'/'+file)
        print('||'+file+'||'+' Complete||')

    def organize(self):
        photos = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.extensions)
        ]
        for name in photos:
            self.movePhoto(name)


# execute
PO = PhotoOrganizer()
PO.organize()
