import urllib.error
import urllib.request

import xmltodict

URL: str = "https://www.pirati.cz/feed.xml"


class DataBase:
    """
    Class for emulating database.

    Downloads .xml file from URL, parse it and emulates read-only database.
    """

    def __init__(self: 'DataBase') -> None:
        with urllib.request.urlopen(URL) as origin:
            resource: bytes = origin.read()
        self.data = xmltodict.parse(resource.decode('utf-8'))
