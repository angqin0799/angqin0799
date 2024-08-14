from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
        assert convert("9:00 AM - 5:00 PM")
        assert convert("9 AM - 5 PM")
        assert convert("from 9 AM to 5 PM")
        assert convert("9AM to 5PM")

def test_time_range():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM")
        assert convert("8:60 AM to 4:60 PM")
        assert convert("21:00 PM to 17:00 PM")
        assert convert("00:00 AM to 00:00 PM")

def test_am_to_am():
    assert convert("9 AM to 5 AM") == "09:00 to 05:00"
    assert convert("9:00 AM to 5:00 AM") == "09:00 to 05:00"
    assert convert("9:30 AM to 5:59 AM") == "09:30 to 05:59"

def test_pm_to_pm():
    assert convert("9 PM to 5 PM") == "21:00 to 17:00"
    assert convert("9:00 PM to 5:00 PM") == "21:00 to 17:00"
    assert convert("9:30 PM to 5:59 PM") == "21:30 to 17:59"

def test_am_to_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:59 PM") == "09:30 to 17:59"

def test_pm_to_am():
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("9:30 PM to 5:59 AM") == "21:30 to 05:59"

def test_midnight():
    assert convert("12 AM to 1 AM") == "00:00 to 01:00"
    assert convert("1 PM to 12 AM") == "13:00 to 00:00"
    assert convert("12 AM to 12:30 AM") == "00:00 to 00:30"

def test_noon():
    assert convert("12 PM to 1 AM") == "12:00 to 01:00"
    assert convert("1 PM to 12 PM") == "13:00 to 12:00"
    assert convert("12 PM to 12:30 PM") == "12:00 to 12:30"
