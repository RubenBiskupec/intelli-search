import PyPDF2
import os

path = '/Users/rubenbiskupec/Desktop/intelli-search/documents1/'
files = os.listdir(path)

for index, file in enumerate(files):
    ### 0 + document.pdf ---> 0document.pdf
    sourceFile = str(index) + 'document.pdf'
    file = path + sourceFile
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    x = pdfReader.numPages
    pageObj = pdfReader.getPage(x-1)
    text = pageObj.extractText()

    dest = str(index) + 'document.txt'
    destPath = path + dest
    destFile = open(destPath, "a")
    destFile.writelines(text)
    destFile.close()



#####
### IMPORTANT ###
### run rename-files.py in srcFolder first !!
### run pdf-to-image.py 
# insert your srcFolder and dstFolder here
srcFolder = '/Users/rubenbiskupec/Desktop/intelli-search/documents1/documenti/'
dstFolder = '/Users/rubenbiskupec/Desktop/intelli-search/documents3/'
