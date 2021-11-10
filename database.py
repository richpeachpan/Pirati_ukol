import traceback
import urllib.error
import urllib.request

import xmltodict

URL: str = "https://www.pirati.cz/feed.xml"


class DataBaseException(Exception):

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
        try:
            with urllib.request.urlopen(URL) as origin:
                resource: bytes = origin.read()
        except urllib.error.HTTPError as exception:
            raise DataBaseException("HTTP error while working with DB:" + str(
                exception.code))
        except urllib.error.URLError as exception:
            raise DataBaseException("URL error while working with DB:" +
                                    exception.reason)
        except Exception:
            raise DataBaseException("Unknown error while working with DB" +
                                    traceback.format_exc())
        self.data = xmltodict.parse(resource.decode('utf-8'))
