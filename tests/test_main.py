from itertools import combinations

import pytest
from dotenv import load_dotenv
from faker import Faker

from pearson_pdf.__main__ import parse_args, run


load_dotenv()


@pytest.fixture
def faker() -> Faker:
    return Faker()  # type: ignore


def test_parse_args() -> None:
    with pytest.raises(SystemExit):
        parse_args()

    parse_args(["qwerty"])
    parse_args(["qwerty", "-i"])
    parse_args(["qwerty", "-u"])

    mutually_exclusive_args = ["-u", "-i", "book.pdf"]
    mutually_exclusive_combinations = combinations(mutually_exclusive_args, 2)
    for combination in mutually_exclusive_combinations:
        with pytest.raises(SystemExit):
            parse_args(list(combination).insert(0, "qwerty"))

    with pytest.raises(SystemExit):
        parse_args(["--version"])
