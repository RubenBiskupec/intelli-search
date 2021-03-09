from flask import Blueprint, render_template
from flask_restplus import Api

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