import PyPDF2
import os

path = '/Users/rubenbiskupec/Desktop/intelli-search/documents1/'
files = os.listdir(path)

# sourceFile = '0document.pdf'
# file = path + sourceFile
# pdfFileObj = open(file, 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# x = pdfReader.numPages
# pageObj = pdfReader.getPage(x-1)
# text = pageObj.extractText()


# destFile = open("/Users/rubenbiskupec/Desktop/intelli-search/documents2/0document.txt", "a")
# destFile.writelines(text)
# destFile.close()

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

per ogni cartella in srcFolder
    apri cartella 
    crea file txt in dst
    per ogni immagine in cartella 
        converti in text
        aggiungi allo stesso file in dstFolder