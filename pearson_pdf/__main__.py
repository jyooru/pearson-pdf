import argparse
from typing import Union

from . import __version__, combine_pages, download_pages, get_book_id, get_book_url


def parse_args(args: "list[str]" = []) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pearson_pdf", description="Download Pearson books as PDFs."
    )
    parser.add_argument("book", type=str, help="Book ID or URL")
    parser.add_argument("--version", action="version", version=__version__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--url", action="store_true", help="Print Book URL")
    group.add_argument("-i", "--id", action="store_true", help="Print Book ID")
    group.add_argument("save_path", type=str, help="Path to save PDF", nargs="?")
    if len(args) == 0:
        return parser.parse_args()
    else:
        return parser.parse_args(args)


def run(args: argparse.Namespace) -> Union[str, None]:
    if args.url:
        return get_book_url(args.book)
    elif args.id:
        return get_book_id(args.book)
    else:
        if args.save_path is None:
            args.save_path = get_book_id(get_book_url(args.book)) + ".pdf"
        args.book = get_book_id(args.book)
        combine_pages(download_pages(args.book), args.save_path)
        return None


def main(args: "list[str]" = []) -> None:
    result = run(parse_args(args))
    if result is not None:
        print(result)


if __name__ == "__main__":
    main()
