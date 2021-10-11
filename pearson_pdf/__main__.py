import argparse
import json
from types import coroutine

from rich.console import Console
from rich.syntax import Syntax
import time
from . import Browser, __version__, combine_pages, download_pages

console = Console()


def parse_args(args: "list[str]" = []) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pearson_pdf", description="Download Pearson books as PDFs."
    )
    parser.add_argument("book", type=str, help="Book URL (foxitAssetURL)")
    parser.add_argument("save_path", type=str, help="PDF save path")
    parser.add_argument("--version", action="version", version=__version__)
    if len(args) == 0:
        return parser.parse_args()
    else:
        return parser.parse_args(args)


def main(args: "list[str]" = []) -> None:
    # parsed_args = parse_args(args)
    # combine_pages(download_pages(parsed_args.book), parsed_args.save_path)
    with console.status("[bold]Launching browser..."):
        browser = Browser()
        console.log("Successfully launched browser.")
    with console.status(
        "[bold]Waiting for reader to be detected...[/bold] \n  Using the browser, login to Pearson and open the book you would like to download. You may need to close all other tabs in the browser for the reader to be detected."
    ):
        browser.wait_for_reader()
        console.log("Successfully detected reader web app.")
    with console.status("[bold]Gathering information..."):
        attempts = 40  # * 0.25 = 10 seconds
        title = browser.get_localStorage("title", attempts)
        page_mapping = json.loads(browser.get_localStorage("_pageMapping", attempts))
        course_id = browser.get_localStorage("courseId", attempts)
        book_id = browser.get_localStorage("bookId", attempts)
        manifest_data = json.loads(
            browser.get_sessionStorage(f"{course_id}_manifestData", attempts)
        )
        page_count = manifest_data["PageCount"]
        page_info = manifest_data["PagesInfo"]
        asset_url = browser.get_variable("foxitAssetURL", attempts)

    browser.browser.close()


if __name__ == "__main__":
    main()
