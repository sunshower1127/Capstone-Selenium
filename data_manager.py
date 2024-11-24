from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from data_types import Article
from translator import translate_one

data_path = Path("articles.json")


def article_to_dict(article: Article):
    return asdict(article)


def dict_to_article(data: dict):
    return Article(**data)


def read_articles():
    data_path.touch()
    with data_path.open() as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    return [dict_to_article(d) for d in data]


def write_articles(articles: list[Article]):
    data = [article_to_dict(article) for article in articles]
    with data_path.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_articles_headers():
    articles: list[Article] = read_articles()
    return [
        {
            "title": article.title,
            "subtitle": article.subtitle,
            "author": article.author,
            "date": article.date,
        }
        for article in articles
    ]


def get_articles():
    return read_articles()


def get_article(index: int):
    articles = read_articles()
    article = articles[index]

    if article.body_type == "en":
        translated = translate_one(article.body)
        article.body = translated
        article.body_type = "kr"

    write_articles(articles)

    article = article_to_dict(article)
    del article["body_type"]
    del article["en_title"]
    return article


if __name__ == "__main__":
    print(get_articles_headers())
