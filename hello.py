from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)



class HelloWorldResource(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'msg': 'post hello world'}

# @app.route('/')
# def hello():
#     return '<h1>Hello'

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return 'Welcome to My Watchlist!'