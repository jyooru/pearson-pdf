import os

import pytest
from dotenv import load_dotenv

from pearson_pdf import PageDownloadError, Browser
from pearson_pdf.__main__ import main, parse_args


load_dotenv()


def test_parse_args() -> None:
    with pytest.raises(SystemExit):
        parse_args()
    with pytest.raises(SystemExit):
        parse_args(["https://foo"])
    parse_args(["https://foo", "foo.pdf"])
    with pytest.raises(SystemExit):
        parse_args(["--version"])


@pytest.mark.skipif(
    "TESTS_BOOK_URL" not in os.environ, reason="TESTS_BOOK_URL is not set"
)
def test_main() -> None:
    with pytest.raises(SystemExit):
        main()
    with pytest.raises(PageDownloadError):
        main([os.environ["TESTS_BOOK_URL"] + "/foo", "foo.pdf"])
    main([os.environ["TESTS_BOOK_URL"], "foo.pdf"])


def test_browser() -> None:
    Browser()
