from pearson_pdf import combine_pages
import requests
from io import BytesIO
from PIL import Image
from tempfile import TemporaryDirectory
import os


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
