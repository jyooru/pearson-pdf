import string
from io import BytesIO

import requests
from PIL import Image


__version__ = "1.3.0"


def get_book_id(book_url: str) -> str:
    book_id = book_url
    if "generated" in book_url:
        book_id = book_id.split("generated")[1]
    if "foxit-assets" in book_url:
        book_id = book_id.split("foxit-assets")[0]
    allowed_characters = string.ascii_letters + string.digits + "-"
    return "".join(
        [character for character in book_id if character in allowed_characters]
    )


def get_book_url(book_id: str) -> str:
    return (
        "https://d2f01w1orx96i0.cloudfront.net/resources/products/epubs/generated/"
        + book_id
        + "/foxit-assets/pages/page"
    )


class PageDownloadError(Exception):
    pass


def download_pages(book_id: str, max_pages: int = -1) -> "list[Image.Image]":
    pages: list[Image.Image] = []
    pages_url = get_book_url(book_id)
    while True:
        response = requests.get(pages_url + str(len(pages)))
        if response.status_code == 200:
            pages.append(Image.open(BytesIO(response.content)))
        else:
            break
        if (not max_pages <= -1) and (len(pages) == max_pages):
            break
    if len(pages) == 0:
        raise PageDownloadError("No pages could be downloaded for {}.".format(book_id))
    return pages


def combine_pages(
    pages: "list[Image.Image]", path: str, format: str = "PDF", resolution: int = 100
) -> None:
    page_0 = pages[0]
    pages.pop(0)
    page_0.save(path, format, resolution=resolution, save_all=True, append_images=pages)
