# "Homework" for the Czech Pirate Party

This software is a part of a job application as a software developer for the Czech Pirate Party.

## Introduction

This software is a web service that should take data from https://www.pirati.cz/feed.xml and present them as JSON. It
takes the original XML and transfers information to JSON using entities.

The programming language of the project is python. It uses the Flask framework and its part Flask-RESTful. It is a
microservice, and that is why I am using the Flask framework.

## API

The project contains only one API call.

### Feed

This call returns feed information.

**GET :** __/feed.json__.

Returns:

```json
    {
  "entries": [
    {
      "author": null,
      "categories": [
        "blog",
        "vláda"
      ],
      "content": "<p>Praha, 11. listopadu 2021 – Piráti zí....",
      "id": "https://www.pirati.cz/tiskove-zpravy/hlasovani-o-ucasti-ve-vlade",
      "media_content": {
        "type": "image",
        "url": "https://www.pirati.cz/assets/img/articles/2021/pirati-forum.jpg"
      },
      "published": "2021-11-11T00:00:00-06:00",
      "summary": "Praha, 11. listopadu 2021 – ...",
      "thumbnail": "https://www.pirati.cz/assets/img/articles/2021/pirati-forum.jpg",
      "title": "Piráti během víkendu rozhodnou o své účasti ve vládě",
      "updated": "2021-11-11T00:00:00-06:00",
      "url": "https://www.pirati.cz/tiskove-zpravy/hlasovani-o-ucasti-ve-vlade.html"
    }
  ],
  "entry_len": 1,
  "page_info": {
    "id": "https://www.pirati.cz/feed.xml",
    "links": [
      {
        "rel": "self",
        "url": "https://www.pirati.cz/feed.xml"
      },
      {
        "rel": "alternate",
        "url": "https://www.pirati.cz/"
      }
    ],
    "subtitle": "Prosazujeme fungující moderní politiku...",
    "title": "Pirátská strana",
    "updated": "2021-11-11T09:52:25-06:00"
  }
}
```

| Name | Type | Description |
| ----------- | ----------- |---------|
| entries | List[[Entry](#entry)] | Entries list (articles for feed) |
| entry_len | int | The number of entries |
| page_info | [PageInfo](#pageinfo) | General information about the feed page|

#### Entry

Entry is a data structure for entry information.

```json
    {
  "author": null,
  "categories": [
    "blog",
    "vláda"
  ],
  "content": "<p>Praha, 11. listopadu 2021 – Piráti zí....",
  "id": "https://www.pirati.cz/tiskove-zpravy/hlasovani-o-ucasti-ve-vlade",
  "media_content": {
    "type": "image",
    "url": "https://www.pirati.cz/assets/img/articles/2021/pirati-forum.jpg"
  },
  "published": "2021-11-11T00:00:00-06:00",
  "summary": "Praha, 11. listopadu 2021 – ...",
  "thumbnail": "https://www.pirati.cz/assets/img/articles/2021/pirati-forum.jpg",
  "title": "Piráti během víkendu rozhodnou o své účasti ve vládě",
  "updated": "2021-11-11T00:00:00-06:00",
  "url": "https://www.pirati.cz/tiskove-zpravy/hlasovani-o-ucasti-ve-vlade.html"
}
```

| Name | Type | Description |
| ----------- | ----------- |---------|
| author | str | Author name |
| categories | List[str] | Entry category list |
| content | str | The entry content  |
| id | str | The entry ID |
| media_content | [MediaContent](#mediacontent)| Stores media for the entry|
| published | str | Publishing DateTime |
| summary | str | The entry summary |
| thumbnail | str | The URL to the entry thumbnail image |
| title | str | The entry title |
| updated | str | Last update DateTime |
| url | str | Url to entry (article)|

#### PageInfo

PageInfo is a data structure for information about the page that stores feed.

```json
    {
  "id": "https://www.pirati.cz/feed.xml",
  "links": [
    {
      "rel": "self",
      "url": "https://www.pirati.cz/feed.xml"
    },
    {
      "rel": "alternate",
      "url": "https://www.pirati.cz/"
    }
  ],
  "subtitle": "Prosazujeme fungující moderní politiku...",
  "title": "Pirátská strana",
  "updated": "2021-11-11T09:52:25-06:00"
}
```

| Name | Type | Description |
| ----------- | ----------- |---------|
| id | str | The page ID |
| links | List[[Link](#link)] | The feed page list of links |
| subtitle | str | The page subtitle |
| title | str | The page title |
| updated | str | Last update of the page |

#### MediaContent

Media content is a data structure for media content information.

```json
    {
  "type": "image",
  "url": "https://www.pirati.cz/assets/img/articles/2021/pirati-forum.jpg"
}
```

| Name | Type | Description |
| ----------- | ----------- |---------|
| type | str | The Media type |
| url | str | The URL to the media |

#### Link

Link is a data structure for information about the link.

```json
    {
  "rel": "self",
  "url": "https://www.pirati.cz/feed.xml"
}
```

| Name | Type | Description |
| ----------- | ----------- |---------|
| rel | str | The relationship between the page and the link |
| url | str | The URL of the link |