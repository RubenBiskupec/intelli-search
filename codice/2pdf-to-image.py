# 2 Transform PDF to image, in order to use Tesseract to convert it to text
# (Conventional pdf to text converters were not working fine because of text in images,
#  links and diagrams)
# pip install pdf2image
from pdf2image import convert_from_path
import os
### IMPORTANT ###
### run rename-files.py in srcFolder first !!
# insert your srcFolder and dstFolder here
srcFolder = '/Users/rubenbiskupec/Desktop/intelli-search/documents1/documenti/'
dstFolder = '/Users/rubenbiskupec/Desktop/intelli-search/documents2/'

files = os.listdir(srcFolder)

for index, file in enumerate(files):
    # goes trough files in numerical order
    srcFile = str(index) + 'document.pdf'
    print("Processing ", srcFile)
    newFile = srcFolder + srcFile
    pages = convert_from_path(newFile, 500)
    newFolder = dstFolder + str(index) + 'document/'
    try:
        os.mkdir(newFolder)
    except OSError:
        print ("Creation of the directory failed")
    else:
        print ("Successfully created the directory")
    i = 0
    for page in pages:
        image = newFolder + str(i) + 'image.png'
        page.save(image, 'PNG')
        print("Processing page n", i)
        i = i+1


