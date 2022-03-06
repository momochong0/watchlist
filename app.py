from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/toutiao'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class HelloWorldResource(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'msg': 'post hello world'}


api.add_resource(HelloWorldResource, '/', endpoint="HelloWorld")
app.config.from_object(Config)

# 此处启动对于1.0之后的Flask可有可无
if __name__ == '__main__':
    app.run(debug=True)