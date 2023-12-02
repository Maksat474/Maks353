import asyncio
from parsel import Selector
import httpx


MAIN_URL = "https://www.house.kg"


def get_html(url):
    response = httpx.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


def get_title(selector: Selector):
    title = selector.css("title::text").get()
    print(title)


def get_all_catalog_items(selector: Selector):
    items = selector.css(".category-block-content a")
    return items


def clean_text(text):
    result = text.strip().replace("\n", "").replace("\t", "")
    result = ' '.join(result.split())
    if result[-1] == " ,":
        result.replace(" ,", "")
    return result


def main():
    html = get_html(MAIN_URL)
    selector = Selector(text=html)
    # get_title(selector)
    items = get_all_catalog_items(selector)
    for item in items:
        title = clean_text(item.css(".main-title::text").get())
        print(title)
        url = item.css("::attr(href)").get()
        print(f"{MAIN_URL}{url}")


if __name__ == "__main__":
    main()

