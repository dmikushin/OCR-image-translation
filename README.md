## Prerequisites

```
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install pytesseract googletrans
wget https://github.com/tesseract-ocr/tessdata/raw/master/fra.traineddata
```

## Usage

```
TESSDATA_PREFIX=$(pwd) python TranslateImageText.py /path/to/images
```

## Background

The script uses a text image (i.e. French) from an open source such as Gutenberg and then uses pytesseract to extract its text using OCR and feeds this text into google translate for translation from the French language into English.
Once the translation is done, it can be viewed in your text editor (i.e. SublimeText)
Note: The script will check all the files ending with ".png" and attempt to extract the text from them

## Sample Images
![extract01.png](https://github.com/skociu/OCR-image-translation/blob/master/extract01.png)

![extract02.png](https://github.com/skociu/OCR-image-translation/blob/master/extract02.png)

![extract03.png](https://github.com/skociu/OCR-image-translation/blob/master/extract03.png)

## Translated Image Texts

[translated_extract01.txt](https://github.com/skociu/OCR-image-translation/blob/master/translated_extract01.txt)

[translated_extract02.txt](https://github.com/skociu/OCR-image-translation/blob/master/translated_extract02.txt)

[translated_extract03.txt](https://github.com/skociu/OCR-image-translation/blob/master/translated_extract03.txt)

## Sources

Gutenberg http://www.gutenberg.org/files/41211/41211-h/41211-h.htm
