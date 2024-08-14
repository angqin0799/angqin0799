from plates import is_valid

def test_start_with_two_letters():
    assert is_valid("AB123") == True
    assert is_valid("1AB23") == False
    assert is_valid("A1") == False
    assert is_valid("AB") == True
    assert is_valid("123") == False

def test_valid_length():
    assert is_valid("AB") == True
    assert is_valid("abc123") == True
    assert is_valid("A") == False
    assert is_valid("AB12345") == False

def test_sandwich_numbers():
    assert is_valid("abcd12") == True
    assert is_valid("ab12cd") == False
    assert is_valid("a1b2cd") == False

def test_zero_first():
    assert is_valid("ab102") == True
    assert is_valid("AB012") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_non_alphanumeric():
    assert is_valid("xyz890") == True
    assert is_valid("ab 123") == False
    assert is_valid("AB123!") == False
    assert is_valid("AB") == True

def test_is_valid():
    assert is_valid("AB123") == True
    assert is_valid("A1B23") == False
    assert is_valid("AB023") == False
    assert is_valid("ABCD") == True
    assert is_valid("ABC1234") == False
