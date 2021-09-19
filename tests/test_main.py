import pytest
from dotenv import load_dotenv
from faker import Faker

from pearson_pdf.__main__ import parse_args, run


load_dotenv()


@pytest.fixture
def faker():
    return Faker()


def test_parse_args():
