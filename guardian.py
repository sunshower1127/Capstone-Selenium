from sw_selenium.driver import SwChrome


def get_guardian_articles():
    web = SwChrome("headless", timeout=10)
    web.set_window_size(600, 1080)

    URL = "https://www.theguardian.com/environment/climate-crisis"

    web.get(URL)

    lst = []

    links = (
        web.find(id="container-climate-crisis")
        .find_all(tag="a")
        .filter("self::*[not(contains(@data-link-name, 'media'))]")
    )

    for link in links:
        web.wait(2)
        link.click()
        title = web.find(tag="h1").text
        subtitle = web.find("//*[@data-gu-name='standfirst']").text
        author = web.find(tag="address").text
        date = web.find(class_name="dcr-1pexjb9").text.split("\n")[0]

        body = "\n".join(web.find(id="maincontent").down[0].find_all(tag="p").text)
        if body.find("\n") == 1:
            body = body[0] + body[2:]

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

        web.back()

    print("\n", len(lst), "articles are collected.")
    return lst
