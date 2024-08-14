from um import count

def test_words_with_um():
    assert count("umbrella") == 0
    assert count("yummy") == 0
    assert count("datum") == 0

def test_sentences():
    assert count("um... hello, um, it's nice to meet you. ") == 2
    assert count("Um, today, um, I think it is, um... sunny.") == 3
    assert count(" um - I found the instrument") == 1

def test_case_sensitivity():
    assert count("UM") == 1
    assert count("Um, hi there!") == 1
    assert count("um. Um... UM!") == 3
