from flask import jsonify
from flask_restful import Resource

from database import DataBase


class Feed(Resource):

    def __init__(self):
        self.__data_source = DataBase()

    def get(self):
        return jsonify(self.__data_source.data)
