# 4 Pre processing text operations

import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string
import os
from contextlib import redirect_stdout

# myFile = "/Users/rubenbiskupec/Desktop/intelli-search/documents3/0document.txt"
# file_content = open(myFile).read()

srcFolder = '/Users/rubenbiskupec/Desktop/intelli-search/documents3/'
dstFolder = '/Users/rubenbiskupec/Desktop/intelli-search/tokens/'

files = os.listdir(srcFolder)


for index, file in enumerate(files):
    srcFile = str(index) + 'document.txt'
    newFile = srcFolder + srcFile
    srcFile = str(index) + 'tokens.txt'
    dstFile = dstFolder + srcFile
    print("Tokenizing ", newFile)
    file_content = open(newFile).read()
    #1 TOKENIZE
    tokens1 = nltk.word_tokenize(file_content)
    #2 EMILINATE STOPWORDS
    tokens2 = []
    wnl = nltk.WordNetLemmatizer()
    for token in tokens1:
        if not token in stopwords.words('english'):
            tokens2.append(token)
    #3 STEMMING
    #The 'english' stemmer is better than the original 'porter' stemmer
    snowball = SnowballStemmer("english")
    tokens3 = []
    for token in tokens2:
        tokens3.append(snowball.stem(token))
    #4 REMOVE PUNCTUATION
    tokens4 = []
    for token in tokens3:
        if (token not in string.punctuation):
            tokens4.append(token)
    wrtFile = open(dstFile, "x")
    with redirect_stdout(wrtFile):
        print(tokens4)
    wrtFile.close()
print("Done")







