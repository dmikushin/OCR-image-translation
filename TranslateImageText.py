from PIL import Image
import pytesseract
import os
import sys
import subprocess
from googletrans import Translator

class Translation:
    '''The script uses a text image (i.e. French) from an open source such as Gutenberg and then uses pytesseract to extract its text using OCR and feeds this text into google translate for translation from the French language into English.
    Once the translation is done, it can be viewed in your text editor (i.e. SublimeText)'''
    def __init__(self, *a):
        self.pytesseract_image_language = pytesseract_image_language
        self.from_language = from_language
        self.to_language = to_language
        self.extract_img = extract_img
        self.extract_file = extract_file
        self.translate_file = translate_file
        self.translator = Translator()

    def extract_image_text(self):
        #https://github.com/tesseract-ocr/tesseract/wiki/Data-Files
        #The link above will give you language codes to use 
        #i.e. code 'fra' = French; 'sqi' = Albanian; 'eng' = English
        pytesseract_image_language = self.pytesseract_image_language
        img = Image.open(self.extract_img)
        text = pytesseract.image_to_string(img, lang=pytesseract_image_language)
        text = text.replace('\n', '\n ')
        text = text.replace('\n', '')
        text = text.replace('.', '.\n')
        text = text.replace('!', '!\n')
        text = text.replace('?', '?\n')
        print(text)
        return text

    def translate_image_text(self, text):
        #for more information on googletrans
        #http://py-googletrans.readthedocs.io/en/latest/
        #Note: type print(googletrans.LANGUAGES) to see supported languages
        # i.e. 'fr' = French; 'sq' = Albanian; 'en' = English
        translation = self.translator.translate(text, 
            src=self.from_language, dest=self.to_language)
        return translation.text

    def write_image_text(self):
        f = open(self.extract_file, 'w')
        f.write(self.extract_image_text())
        f.close()

    def remove_extract_file(self):
        os.remove(self.extract_file)


    def write_translation(self):
        f1 = open(self.extract_file, 'r')
        with open(self.translate_file, 'w') as f:
            for i, line in enumerate(f1, 1):
                f.write(str(i) + ') ' + line)
                f.write(str(i) + ') ' + self.translate_image_text(line)+ '\n\n')
        f.close()

    def view_translation(self):
        subprocess.Popen(['subl', self.translate_file])

    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: ./ocrtrans <folder_path>")
        sys.exit(0)

    path = sys.argv[1]
    pytesseract_image_language = 'fra'
    from_language = 'fr'
    to_language = 'en'

    for dirpath, _, filenames in os.walk(path):
        for filename in sorted(filenames):
            f = os.path.abspath(os.path.join(dirpath, filename))
            if f.endswith(".jpeg"):
                extract_img = "{}".format(f)
                extract_file = os.path.join(dirpath, "{}.txt".format(filename))
                translate_file = os.path.join(dirpath, "{}_translated.txt".format(filename))
                t=Translation()
                t.extract_image_text()
                #t.write_image_text()
                #t.write_translation()
                #t.remove_extract_file()
                #t.view_translation()
                print("{} OK".format(f))

