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
    def __init__(self, info: Dict[str, str]):
        self.info: Dict[str, str] = info


class FeedPage:
    """
    FeedPage entity

    Stands for FeedPage and stores info about page and all articles on page
    """
    def __init__(self, info: Dict[str, str], entry: List[Article]):
        self.info: Dict[str, str] = info
        self.entry: List[Article] = entry
