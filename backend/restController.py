from flask import Blueprint, render_template, request
from flask_restplus import Api, Resource



from whoosh.index import create_in, open_dir 
from whoosh.fields import *
import os, os.path
from whoosh.qparser import QueryParser
import whoosh.index as index


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
    return render_template('home.html')

@bp.route('/query', methods=['GET', 'POST'])
def query():
    query = request.args.get('query')
    
    print("calling finder ")
    results = finder(query)
    print("results ", results)
    return str(results)

def finder(query):
    print(query)
    ix = index.open_dir("../codice/indexdir")
    qp = QueryParser("content", schema=ix.schema)
    q = qp.parse(u"magnitud")

    with ix.searcher() as s:
      results = s.search(q)
      
      #print (results[0])
      return results