from flask import Blueprint, render_template, request
from flask_restplus import Api, Resource

from whoosh.index import create_in, open_dir 
from whoosh.fields import *
import os, os.path
from whoosh.qparser import QueryParser
import whoosh.index as index
from whoosh import scoring

bp = Blueprint("restController", __name__)

api = Api(bp)
api_v1 = api.namespace('api/v1', description='Main api')

# a simple page that says hello
@bp.route('/hello')
def hello():
    return 'Hello, World!'

@bp.route('/ping')
def pong():
    return 'pong'

@bp.route('/home')
@bp.route('/search')
def home():
    return render_template('search.html')

@bp.route('/query', methods=['GET', 'POST'])
def query():
    query = request.args.get('query')
    
    print("calling finder ")
    token_paths, highlights = finder(query)
    doc_paths = replace_tokens_with_docs(token_paths)
    docs = read_docs_from_paths(doc_paths, highlights, query)
    return render_template("docs.html", context=docs, dym="dym")

def finder(query):
    print(query)
    ix = index.open_dir("../codice/indexdir")
    qp = QueryParser("content", schema=ix.schema)
    q = qp.parse(query)
    paths = []
    highlights = []
    print("Finder query ", query)
    with ix.searcher(weighting=scoring.TF_IDF()) as s:
        results = s.search(q)
        highlights = []
        for result in results:
            paths.append(result["title"])

            url = result["title"].split('/')
            url = url[5:]
            url = str(url[0]) + "/" + str(url[1])
            url = "./static/" + url
            url = url.replace("tokens/", "documents3/")
            url = url.replace("tokens", "document")
    
            with open(url) as file:
                file_contents = file.read()
            highlights.append(result.highlights("content", text=file_contents))
    
    return paths, highlights

def replace_tokens_with_docs(tokens):
    docs = []
    for token in tokens:
        token = token.replace("tokens", "documents3")
        token = token.replace("token", "document")
        token = token.replace("documents3.txt", "document.txt")
        docs.append(token)
    return docs 

def read_docs_from_paths(paths, highlights, query):
    docs = []
    i = 0
    query = query.split(" ")
    print("Splitting")
    for term in query:
        print(term)
    terms = ""
    words = ""
    for term in query:
        if (term != " "):
            terms = terms + term + "_"
            words = words + term + " "
    thes = "https://cso.kmi.open.ac.uk/topics/" + terms
    thes = thes[:-1]
    for path in paths:
        doc = {}
        summary = highlights[i] 
        url = path.split('/')
        url = url[5:]
        url = str(url[0]) + "/" + str(url[1])
        url = "../static/" + url
        doc.update({"high": summary, "url": url, "thes": thes, "terms": words})
        docs.append(doc)
        i += 1
    return docs
