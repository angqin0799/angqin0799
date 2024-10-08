from calculator import square
import pytest

# ''' assert '''

# def main():
#     test_square()

# def test_square():
#         assert square(2) == 4
#         assert square(3) == 9

# if __name__ == "__main__":
#     main()

''' using pytest '''
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


