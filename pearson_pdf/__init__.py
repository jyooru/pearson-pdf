import requests
from io import BytesIO
from PIL import Image
import string


def book_id(book_url: str):
    book_id = book_url
    if "generated" in book_url:
        book_id = book_id.split("generated")[1]
    if "foxit-assets" in book_url:
        book_id = book_id.split("foxit-assets")[0]
    allowed_characters = string.ascii_letters + string.digits + "-"
    return "".join(
        [character for character in book_id if character in allowed_characters]
    )


def book_url(book_id: str):
    return (
        "https://d2f01w1orx96i0.cloudfront.net/resources/products/epubs/generated/"
        + book_id
        + "/foxit-assets/pages/page"
    )


def download_pages(book_id: str):
    pages = []
    pages_url = book_url(book_id)
    while True:
        response = requests.get(pages_url + str(len(pages)))
        if response.status_code == 200:
            pages.append(Image.open(BytesIO(response.content)))
        elif response.status_code == 403:
            break
        else:
            raise Exception('unexpected status code "' + response.status_code + '"')
    return pages


def combine_pages(pages: list, path: str, format: str = "PDF", resolution: int = 100):
    page_0 = pages[0]
    pages.pop(0)
    page_0.save(path, format, resolution=resolution, save_all=True, append_images=pages)
