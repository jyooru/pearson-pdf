import requests
import tempfile
import io
from PIL import Image


textbook_id = ""
output_path = "output.pdf"


def textbook_url(id: str):
    return (
        "https://d2f01w1orx96i0.cloudfront.net/resources/products/epubs/generated/"
        + id
        + "/foxit-assets/pages/page"
    )


with tempfile.TemporaryDirectory() as tmpdir:
    page = 0
    pages = []
    while True:
        print("downloading page " + str(page))
        response = requests.get(textbook_url(textbook_id) + str(page))
        if response.status_code == 200:
            pages.append(Image.open(io.BytesIO(response.content)))
            page += 1
        elif response.status_code == 403:
            print("got 403 for page " + str(page) + ", not downloading anymore pages")
            break
        else:
            raise Exception('unexpected status code "' + response.status_code + '"')

    page_0 = pages[0]
    pages.pop(0)
    print('saving pdf to "' + output_path + '"')
    page_0.save(
        output_path, "PDF", resolution=100.0, save_all=True, append_images=pages
    )
