import json

from data_manager import get_articles
from data_types import Article
from sw_selenium.driver import SwChrome
from translator import translate_date, translate_many


def get_guardian_articles():
    web = SwChrome("headless", timeout=10)
    web.set_window_size(600, 1080)

    URL = "https://www.theguardian.com/environment/climate-crisis"

    web.get(URL)

    lst: list[Article] = []

    cnt = len(
        web.find(id="container-climate-crisis")
        .find_all(tag="a")
        .filter("self::*[not(contains(@data-link-name, 'media'))]")
    )

    existing_articles = get_articles()

    for i in range(cnt):
        web.find(id="container-climate-crisis").find_all(tag="a").filter(
            "self::*[not(contains(@data-link-name, 'media'))]"
        )[i].click()
        en_title = web.find(tag="h1").text

        for article in existing_articles:
            if article.en_title == en_title:
                lst.append(article)
                print(article.title, "is already collected.")
                break

        else:  # no break = not found = doesn't exist
            en_subtitle = web.find("//*[@data-gu-name='standfirst']").text
            en_subtitle = en_subtitle.split("\n")[0]
            en_author = web.find(tag="address").text
            title, subtitle, author = translate_many(en_title, en_subtitle, en_author)

            en_date = web.find(class_name="dcr-1pexjb9").text.split("\n")[0]
            date = translate_date(en_date)

            paragraphs = web.find(id="maincontent").down[0].find_all(tag="p").text
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

            print(title, "is collected.")

        web.get(URL)

    print("\n", len(lst), "articles are collected.\n")
    return lst


if __name__ == "__main__":
    print(len(json.dumps(get_guardian_articles())))
