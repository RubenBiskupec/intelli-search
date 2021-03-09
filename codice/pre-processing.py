import nltk
import os


# TOKENIZATION
# path = '/Users/rubenbiskupec/Desktop/intelli-search/documents'
# folder = os.listdir(path)
# doc = path + '/0document.pdf'
# document = open("/Users/rubenbiskupec/Desktop/intelli-search/documents/0document.pdf", "rb")
# print(document.decode('latin-1'))
file = "/Users/rubenbiskupec/Desktop/intelli-search/documents/0document.pdf"
with open(file, "rb") as fopen:
    doc = fopen.read()
    print(doc.decode("latin-1"))

