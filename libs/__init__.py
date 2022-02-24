from tabnanny import check
from pytesseract import pytesseract
import cv2
import os


class ImgTxt():
    def __init__(self, path, pathSave):
        super().__init__()

        self.path = os.path.abspath(path)
        self.pathSave = pathSave
        self.alert = "Error, fill in the parameters!"

        if path != "" and pathSave != "":
            self.convert()

    def getName(self, file):
        self.name = file.split("\\")[-1]
        return self.name

    def toTxt(self, text):
        name = self.getName(self.path)
        path = self.pathSave
        if not os.path.isdir(path):
            os.mkdir(path)

        localToSave = f'{path}/{name}.txt'

        with open(localToSave, 'w', encoding="utf8") as file:
            file.write(text)

        self.alert = f"File '{localToSave}' saved successfully!"

        return f"File '{localToSave}' saved successfully!"

    def convert(self):
        try:
            image = self.path
            pathTs = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = pathTs

            img = cv2.imread(image)
            text = pytesseract.image_to_string(img, lang="por")

            self.toTxt(text)

            return text
        except Exception:
            self.alert = "Error, make sure the path has special characters!"
            return "Error, make sure the path has special characters!"


class ImgsTxt():
    def __init__(self, path, pathSave, Output):
        super().__init__()

        self.path = os.path.abspath(path)
        self.pathSave = pathSave
        self.alert = "Error, fill in the parameters!"

        if path != "" and pathSave != "":
            self.convert(Output)

    def getExt(self, file):
        index = file.rfind('.')
        return file[index:]

    def convert(self, Output):
        try:
            exts = ['.png', '.jpg', '.jpeg', '.bmp']
            images = os.listdir(self.path)
            if not os.path.isdir(self.pathSave):
                os.mkdir(self.pathSave)

            if images == []:
                self.alert = "There are no images in the selected directory"
                Output.add(self.alert)
            else:
                checkImg = False
                for image in images:
                    imgPath = os.path.join(self.path, image)
                    ext = self.getExt(image)
                    if ext in exts:
                        checkImg = True
                        convert = ImgTxt(imgPath, self.pathSave)
                        self.alert = convert.alert
                        Output.add(self.alert)
                if checkImg is False:
                    self.alert = "There are no images in the selected directory"
                    Output.add(self.alert)

                self.alert = "\n============== DONE! =============="

        except Exception:
            self.alert = "Error, make sure the path has special characters!"
            Output.add(self.alert)
            return "Error, make sure the path has special characters!"
