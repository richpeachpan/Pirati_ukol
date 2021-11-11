from flask import jsonify, Response
from flask_restful import Resource

from database import DataBase


class FeedPage(Resource):
    """
    Service for feed
    """

    def __init__(self: 'FeedPage') -> None:
        self.__data_source = DataBase()

    def get(self) -> Response:
        """
        Feed get service

        It processed data from data source and return them as
        flask.Response. It supports JSON.

        :return: flask.Response processed data from data source
        """
        return jsonify(self.__data_source.get_full_json())
