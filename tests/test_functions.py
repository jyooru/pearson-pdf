import os
from io import BytesIO
from tempfile import TemporaryDirectory

import pytest
import requests
from dotenv import load_dotenv
from PIL import Image

from pearson_pdf import (
    PageDownloadError,
    combine_pages,
    download_pages,
)


load_dotenv()


def test_combine_pages() -> None:
    def random_images() -> Image:
        return Image.open(
            BytesIO(requests.get("https://source.unsplash.com/random").content)
        )

    images = [random_images() for _ in range(3)]
    with TemporaryDirectory() as tmpdir:
        path = tmpdir + "/output.pdf"
        combine_pages(images, path)
        assert os.path.exists(path)


@pytest.mark.skipif(
    "TESTS_BOOK_URL" not in os.environ, reason="TESTS_BOOK_URL is not set"
)
def test_download_pages() -> None:
    max_pages = 10
    pages = download_pages(os.environ["TESTS_BOOK_URL"], max_pages)
    assert len(pages) == max_pages
    for page in pages:
        assert page.height != 0
        assert page.width != 0

    with pytest.raises(PageDownloadError):
        download_pages(os.environ["TESTS_BOOK_URL"] + "/foo")
