from . import get_book_id, get_book_url, combine_pages, download_pages
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="pearson_pdf", description="Download Pearson books as PDFs."
    )
    parser.add_argument("book", type=str, help="Book ID or URL")
    parser.add_argument("save_path", type=str, help="Path to save PDF")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--url", action="store_true", help="Print Book URL")
    group.add_argument("-i", "--id", action="store_true", help="Print Book ID")
    args = parser.parse_args()

    if args.url:
        print(get_book_url(get_book_id(args.book)))
        exit()
    if args.id:
        print(get_book_id(get_book_url(args.book)))
        exit()
    args.book = get_book_id(args.book)
    combine_pages(download_pages(args.book), args.save_path)


if __name__ == "__main__":
    main()
