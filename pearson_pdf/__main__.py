import argparse

from rich.console import Console

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
        "[bold]Using the browser, login to Pearson and open the book you would like to download. Waiting for reader to be detected..."
    ):
        browser.wait_for_reader()
        console.log("Successfully detected reader web app.")
    browser.browser.close()


if __name__ == "__main__":
    main()
