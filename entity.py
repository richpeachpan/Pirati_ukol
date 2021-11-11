"""
Entities for working with feed

These classes should help working with feed and format it to prettier form
or use only a part of it if it is necessary.
"""

from typing import Dict, List


class Article:
    """
    Article entity

    Stands for article and stores all information about article.
    """

    def __init__(self, data: Dict[str, str]):
        self.title: str = data['title']['#text']
        self.url: str = data['link']['@href']
        self.id: str = data['id']
        self.published: str = data['published']
        self.updated: str = data['updated']
        self.content: str = data['content']['#text']
        self.author: str = data['author']['name']
        self.categories: List[str] = \
            [category['@term'] for category in data['category']]
        self.summary: str = data['summary']['#text']
        self.thumbnail: str = data['media:thumbnail']['@url']
        self.media_content: Dict[str, str] = \
            {'type': data['media:content']['@medium'],
             'url': data['media:content']['@url']}


class FeedPage:
    """
    FeedPage entity

    Stands for FeedPage and stores info about page and all articles on page
    """

    def __init__(self, info: Dict[str, str], entry: List[Article]):
        self.info: Dict[str, str] = info
        self.entry: List[Article] = entry
        self.entry_len: int = len(entry)
