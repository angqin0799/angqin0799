import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("2/3") == 67
    assert convert("0/100") == 0
    assert convert("1/100") == 1

def test_ValueError():
    with pytest.raises(ValueError):
        convert("three/four")
        convert("10/5")
        convert("1.5/2")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_percent_output():
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"

def test_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

