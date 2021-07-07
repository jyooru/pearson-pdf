from . import get_book_id, combine_pages, download_pages
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="pearson_pdf", description="Download Pearson books as PDFs."
    )
    parser.add_argument("book", type=str, help="Book ID or URL")
    parser.add_argument("save_path", type=str, help="Path to save PDF")
    args = parser.parse_args()

    args.book = get_book_id(args.book)
    combine_pages(download_pages(args.book), args.save_path)


if __name__ == "__main__":
    main()
