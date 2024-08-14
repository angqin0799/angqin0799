from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_number():
    '''omits numbers'''
    assert shorten("123tWITter") == "123tWTtr"
    assert shorten("1twi2teerr") == "1tw2trr"

def test_punctuation():
    '''omits punctuation'''
    assert shorten("twi_tter?!") == "tw_ttr?!"
    assert shorten("(tw@at*eriously>?!)") == "(tw@t*rsly>?!)"



