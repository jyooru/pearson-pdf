from pearson_pdf.__main__ import parse_args, run
from dotenv import load_dotenv
import pytest
from faker import Faker


load_dotenv()


@pytest.fixture
def faker():
    return Faker()


def test_parse_args():
