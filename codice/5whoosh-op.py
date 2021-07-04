# 5 Create schema and search 

from whoosh.index import create_in, open_dir 
from whoosh.fields import *
import os, os.path
from whoosh.qparser import QueryParser

srcFolder = '/Users/rubenbiskupec/Desktop/intelli-search/tokens/'

files = os.listdir(srcFolder)
# myFile0 = u"/Users/rubenbiskupec/Desktop/intelli-search/documents3/0document.txt"
# myFile1 = u"/Users/rubenbiskupec/Desktop/intelli-search/documents3/1document.txt"

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT) 

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = create_in("indexdir", schema)

writer = ix.writer()

for i in range (752):
  srcFile = str(i) + 'tokens.txt'
  myFile = srcFolder + srcFile
  try:
    fileobj = open(myFile, encoding='utf-8', errors='ignore')
    content = fileobj.read()
    fileobj.close()
    writer.add_document(title=myFile, content=content)
    print("indexed file n.", i)
  except:
    print("error")
writer.commit()


