from . import get_book_id, get_book_url, combine_pages, download_pages, __version__
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="pearson_pdf", description="Download Pearson books as PDFs."
    )
    parser.add_argument("book", type=str, help="Book ID or URL")
    parser.add_argument("--version", action="version", version=__version__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--url", action="store_true", help="Print Book URL")
    group.add_argument("-i", "--id", action="store_true", help="Print Book ID")
    group.add_argument("save_path", type=str, help="Path to save PDF", nargs="?")
    args = parser.parse_args()
    if args.url or args.id:
        if args.url:
            print(get_book_url(args.book))
        elif args.id:
            print(get_book_id(args.book))
        exit()
    else:
        if args.save_path is None:
            args.save_path = get_book_id(get_book_url(args.book)) + ".pdf"
        args.book = get_book_id(args.book)
        combine_pages(download_pages(args.book), args.save_path)


if __name__ == "__main__":
    main()
