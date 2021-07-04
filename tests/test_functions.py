from pearson_pdf import combine_pages, download_pages
import requests
from io import BytesIO
from PIL import Image
from tempfile import TemporaryDirectory
import os
from dotenv import load_dotenv
import pytest


load_dotenv()


def test_combine_pages():
    def random_images():
        return Image.open(
            BytesIO(requests.get("https://source.unsplash.com/random").content)
        )

    images = [random_images() for _ in range(3)]
    with TemporaryDirectory() as tmpdir:
        path = tmpdir + "/output.pdf"
        combine_pages(images, path)
        assert os.path.exists(path)


@pytest.mark.skipif(os.getenv("book_id") is None, reason="book_id is not set")
def test_download_pages():
    pages = download_pages(os.getenv("book_id"))
    assert len(pages) != 0
    for page in pages:
        assert page.height != 0
        assert page.width != 0
