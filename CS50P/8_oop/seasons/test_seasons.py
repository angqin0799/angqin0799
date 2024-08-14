from seasons import validate, convert, number_to_words
from datetime import date
import pytest

def test_validate():
    assert validate("1999-01-01") == "1999-01-01"

def test_validate_invalid_date():
    with pytest.raises(SystemExit):
        validate("2024.03.08")
        validate("2024-13-01")
        validate("2024-12-32")

def test_convert():
    assert convert(str(date.today())) == 0

def test_number_to_words():
    assert number_to_words(525600) == "Five hundred twenty-five thousand, six hundred"


