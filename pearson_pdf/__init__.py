from io import BytesIO

import requests
from PIL import Image
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


__version__ = "1.3.0"


class Browser:
    def __init__(self, headless=False) -> None:
        self.options = Options()
        if headless:
            self.options.add_argument("--headless")
        self.browser = Firefox(options=self.options)


class PageDownloadError(Exception):
    pass


def download_pages(book_url: str, max_pages: int = -1) -> "list[Image.Image]":
    pages: list[Image.Image] = []
    while True:
        response = requests.get(f"{book_url}/pages/page{str(len(pages))}")
        if response.status_code == 200:
            pages.append(Image.open(BytesIO(response.content)))
        else:
            break
        if (not max_pages <= -1) and (len(pages) == max_pages):
            break
    if len(pages) == 0:
        raise PageDownloadError(f"No pages could be downloaded for {book_url}.")
    return pages


def combine_pages(
    pages: "list[Image.Image]", path: str, format: str = "PDF", resolution: int = 100
) -> None:
    page_0 = pages[0]
    pages.pop(0)
    page_0.save(path, format, resolution=resolution, save_all=True, append_images=pages)
