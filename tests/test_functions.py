import os
from io import BytesIO
from tempfile import TemporaryDirectory

import pytest
import requests
from dotenv import load_dotenv
from faker import Faker
from PIL import Image

from pearson_pdf import (
    PageDownloadError,
    combine_pages,
    download_pages,
    get_book_id,
    get_book_url,
)


load_dotenv()


@pytest.fixture
def faker() -> Faker:
    return Faker()  # type: ignore


def test_get_book(faker: Faker) -> None:
    book_id = faker.uuid4()
    assert get_book_id(get_book_url(book_id)) == book_id


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


@pytest.mark.skipif("book_id" not in os.environ, reason="book_id is not set")
def test_download_pages() -> None:
    max_pages = 10
    pages = download_pages(os.environ["book_id"], max_pages)
    assert len(pages) == max_pages
    for page in pages:
        assert page.height != 0
        assert page.width != 0

    with pytest.raises(PageDownloadError):
        download_pages("qwerty")
