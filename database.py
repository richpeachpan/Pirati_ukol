import traceback
import urllib.error
import urllib.request
from typing import Dict, Any, Union

import xmltodict

from entity import Feed, Article

URL: str = "https://www.pirati.cz/feed.xml"


class DataBaseException(Exception):
    """
    Exception for wrapping exceptions while working with resources

    This exception is for wrapping exceptions from resources which
    database uses. Exceptions are propagated using this wrapper.
    """

    def __init__(self: 'DataBaseException', message: str):
        self.text: str = message

    def __str__(self: 'DataBaseException'):
        return str(self.__class__) + ": " + self.text


class DataBase:
    """
    Class for emulating database.

    Downloads .xml file from URL, parse it and emulates read-only database.
    """

    def __init__(self: 'DataBase') -> None:
        data = self.__get_data()
        self.entry = [Article(article) for article in data.pop("entry", [])]
        self.page = Feed(data)

    def get_full_json(self: 'DataBase') -> Dict[str, Union[str, int]]:
        """
        Returns data as JSON

        :return: Dict Dictionary representing data
        """
        return {'page_info': self.page.__dict__,
                'entries': [elem.__dict__ for elem in self.entry],
                'entry_len': len(self.entry)}

    @staticmethod
    def __get_data() -> Dict[str, Any]:
        """
        Data getter

        Gets data from URL and return them as a one big dictionary

        :throws: DataBaseException wraps all thrown exception as DBException
        :return: Dict[str, Any] Dictionary of info from URL
        """
        # try-catch catch all exceptions and use DBException as wrapper
        try:
            with urllib.request.urlopen(URL) as origin:
                resource: bytes = origin.read()
        except urllib.error.HTTPError as exception:
            raise DataBaseException("HTTP error while working with DB:" +
                                    str(exception.code))
        except urllib.error.URLError as exception:
            raise DataBaseException("URL error while working with DB:" +
                                    exception.reason)
        except Exception:
            raise DataBaseException("Unknown error while working with DB" +
                                    traceback.format_exc())
        data: Dict[str, Any] = \
            xmltodict.parse(resource.decode('utf-8'))["feed"]
        return data
