from data_manager import get_articles
from data_types import Article
from selenium_wrapper_3.builder import ChromeBuilder
from selenium_wrapper_3.node import *  # type: ignore[wildcard]
from selenium_wrapper_3.util import *  # type: ignore[wildcard]
from translator import translate_date, translate_many


def get_guardian_articles():
    ChromeBuilder().set_window_size(600, 1080).headless_setting().build()

    URL = "https://www.theguardian.com/environment/climate-crisis"

    url(URL)

    lst: list[Article] = []

    existing_articles = get_articles()

    for a in populate(
        Div(id="container-climate-crisis")
        // A(("data-link-name", "starts with", "news"))
    ):
        click(a)
        en_title = text(H1())

        for article in existing_articles:
            if article.en_title == en_title:
                lst.append(article)
                print(article.title, "is already collected.")
                break

        else:  # no break
            en_subtitle = text(Div(("data-gu-name", "=", "standfirst")))
            en_subtitle = en_subtitle.split("\n")[0]
            en_author = text(Address())
            title, subtitle, author = translate_many(en_title, en_subtitle, en_author)

            en_date = text(Any(class_="dcr-1pexjb9")).split("\n")[0]
            date = translate_date(en_date)

            paragraphs = [
                text(p) for p in populate(Div(id="maincontent") / Div() // P())
            ]
            paragraphs = [p.replace("\n", "") for p in paragraphs if p]
            en_body = "\n".join(paragraphs)

            lst.append(
                Article(
                    en_title=en_title,
                    title=title,
                    subtitle=subtitle,
                    author=author,
                    date=date,
                    body=en_body,
                )
            )

            print(lst)

        url(URL)

    print("\n", len(lst), "articles are collected.\n")
    return lst
