from . import book_id, combine_pages, download_pages
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="pearson_pdf", description="Download Pearson books as PDFs."
    )
    parser.add_argument(
        "-u", "--url", action="store_true", help="Parse Book ID from URL"
    )
    parser.add_argument("book_id", type=str, help="Book ID used to fetch pages")
    parser.add_argument("save_path", type=str, help="Path to save PDF")
    args = parser.parse_args()

    if args.url:
        args.book_id = book_id(args.book_id)
    combine_pages(download_pages(args.book_id), args.save_path)


if __name__ == "__main__":
    main()
