from sw_selenium.driver import SwChrome


def get_guardian_articles():
    web = SwChrome("headless", timeout=10)
    web.set_window_size(600, 1080)

    URL = "https://www.theguardian.com/environment/climate-crisis"

    web.get(URL)

    lst = []

    cnt = len(
        web.find(id="container-climate-crisis")
        .find_all(tag="a")
        .filter("self::*[not(contains(@data-link-name, 'media'))]")
    )

    for i in range(cnt):
        web.find(id="container-climate-crisis").find_all(tag="a").filter(
            "self::*[not(contains(@data-link-name, 'media'))]"
        )[i].click()
        title = web.find(tag="h1").text
        subtitle = web.find("//*[@data-gu-name='standfirst']").text
        author = web.find(tag="address").text
        date = web.find(class_name="dcr-1pexjb9").text.split("\n")[0]

        paragraphs = web.find(id="maincontent").down[0].find_all(tag="p").text
        paragraphs = [p.replace("\n", "") for p in paragraphs if p]
        body = "\n".join(paragraphs)

        lst.append(
            {
                "title": title,
                "subtitle": subtitle,
                "author": author,
                "date": date,
                "body": body,
            }
        )

        print("\r", title, end="")

        web.get(URL)

    print("\n", len(lst), "articles are collected.\n")
    return lst


if __name__ == "__main__":
    print(get_guardian_articles())
