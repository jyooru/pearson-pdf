import os

import pytest
from dotenv import load_dotenv

from pearson_pdf import PageDownloadError
from pearson_pdf.__main__ import main, parse_args


load_dotenv()


def test_parse_args() -> None:
    with pytest.raises(SystemExit):
        parse_args()
    with pytest.raises(SystemExit):
        parse_args(["foo"])
    parse_args(["foo", "foo.pdf"])
    with pytest.raises(SystemExit):
        parse_args(["--version"])


@pytest.mark.skipif("book_id" not in os.environ, reason="book_id is not set")
def test_main() -> None:
    with pytest.raises(SystemExit):
        main()
    with pytest.raises(PageDownloadError):
        main(["foo", "foo.pdf"])
    main([os.environ["book_id"], "foo.pdf"])
