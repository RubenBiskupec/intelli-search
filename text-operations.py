import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

myFile = "/Users/rubenbiskupec/Desktop/intelli-search/documents3/0document.txt"
file_content = open (myFile).read()

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

# Parsers
# Best is statistical one, based on treebank
# Taggers are better, example: CLAWS,QTAG

# - Thesauri

# - Word similarities 
#     synonyms or similarity (distacnce)
#     - similarity: 
#         path based 
#         information based
# - Word sense disambiguation






