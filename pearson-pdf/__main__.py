import requests
from io import BytesIO
from PIL import Image


textbook_id = ""


def textbook_url(id: str):
    return (
        "https://d2f01w1orx96i0.cloudfront.net/resources/products/epubs/generated/"
        + id
        + "/foxit-assets/pages/page"
    )


def download_pages():
    page = 0
    pages = []
    while True:
        print("downloading page " + str(page))
        response = requests.get(textbook_url(textbook_id) + str(page))
        if response.status_code == 200:
            pages.append(Image.open(BytesIO(response.content)))
            page += 1
        elif response.status_code == 403:
            print("got 403 for page " + str(page) + ", not downloading anymore pages")
            break
        else:
            raise Exception('unexpected status code "' + response.status_code + '"')
    return pages


def combine_pages(pages: list, path: str):
    page_0 = pages[0]
    pages.pop(0)
    print('saving pdf to "' + output_path + '"')
    page_0.save(path, "PDF", resolution=100.0, save_all=True, append_images=pages)


if __name__ == "__main__":
    combine_pages(download_pages(), "output.pdf")
