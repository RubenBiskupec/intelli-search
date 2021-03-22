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

# with open(myFile0, "rb") as f:
#     content = f.readlines()
#     writer.add_document(title=u"First document", path=myFile0, content=content)

# with open(myFile1) as f:
#     content = f.readlines()
#     writer.add_document(title=u"Second document", path=myFile1, content=content)

# print(enumerate(files))
# for index,file in enumerate(files):

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

# def add_doc(writer, path):
#   fileobj = open(path, "rb")
#   content = fileobj.read()
#   fileobj.close()
#   writer.add_document(path=path, content=content)
## Query 

# qp = QueryParser("content", schema=ix.schema)
# q = qp.parse(u"Spaceweather")

# with ix.searcher() as s:
#   results = s.search(q)
#   print (results)
#   print (results[0])

