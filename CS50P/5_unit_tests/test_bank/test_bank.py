from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello there") == 0

def test_h_greetings():
    assert value("hi") == 20
    assert value("how do you do?") == 20

def test_non_h_greetings():
    assert value("good day to you") == 100
    assert value("what's up?") == 100

def test_case_sensitivity():
    assert value("Hello") == 0
    assert value("Hey") == 20
    assert value("What's cookin', good lookin'?") == 100

def test_number():
    assert value("0") == 100
    assert value("-100") == 100
    assert value("Hello 100") == 0
    assert value("Howdy 123") == 20

