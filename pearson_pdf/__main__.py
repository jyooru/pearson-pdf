from . import combine_pages, download_pages
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pearson_pdf", description="Download Pearson books as PDFs."
    )
    parser.add_argument("book_id", type=str, help="Book ID used to fetch pages")
    parser.add_argument("save_path", type=str, help="Path to save PDF")
    args = parser.parse_args()

    combine_pages(download_pages(args.book_id), args.save_path)
