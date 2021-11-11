"""
Entities for working with feed

These classes should help working with feed and format it to prettier form
or use only a part of it if it is necessary.
"""

from typing import Dict, List, Any


class Article:
    """
    Article entity

    Stands for article and stores all information about article.
    """

    def __init__(self, data: Dict[str, Any]):
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


class Feed:
    """
    FeedPage entity

    Stands for FeedPage and stores info about page and all articles on page
    """

    def __init__(self: 'Feed', data: Dict[str, Any]) -> None:
        self.links: List[Dict[str, str]] = \
            [{'rel': link['@rel'], 'url': link['@href']} for link in
             data['link']]
        self.updated: str = data['updated']
        self.id: str = data['id']
        self.title: str = data['title']['#text']
        self.subtitle: str = data['subtitle']
