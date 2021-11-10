from flask import Flask
from flask_restful import Api

from services import Feed

app = Flask(__name__)
api = Api(app)

app.config['JSON_AS_ASCII'] = False

api.add_resource(Feed, "/feed.json")

if __name__ == '__main__':
    app.run(port=8080)
