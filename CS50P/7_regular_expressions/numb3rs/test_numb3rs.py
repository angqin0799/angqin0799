from numb3rs import validate

def test_extremes():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_out_of_range():
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False
    assert validate("-1.300.4/5.-90") == False

def test_non_int():
    assert validate("cat") == False
    assert validate("My IPv4 address is 1.2.3.4") == False
    assert validate("1.2.3.4 is my IPv4 address.") == False

def test_format():
    assert validate("1.1.1") == False
    assert validate("0:255:2:1") == False
    assert validate("1,2,3,4") == False
    assert validate("0000.0000.0000.0000") == False


