from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

app.config['JSON_AS_ASCII'] = False


class Feed(Resource):

    def get(self):
        return {'data': 'Pirati'}


api.add_resource(Feed, "/feed.json")

if __name__ == '__main__':
    app.run(port=8080)
