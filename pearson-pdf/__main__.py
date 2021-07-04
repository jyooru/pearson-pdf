from . import combine_pages, download_pages


if __name__ == "__main__":
    combine_pages(download_pages(), "output.pdf")
