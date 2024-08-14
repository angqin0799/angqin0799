from jar import Jar
import pytest

def test_init():
    jar = Jar()
    jar.deposit(12)
    assert jar.size == 12

    with pytest.raises(ValueError):
        jar = Jar(-100)                 # Negative capacity raises ValueError

    with pytest.raises(ValueError):
        jar = Jar(5)                    # Able to initialize a cookie jar with given capacity
        jar.withdraw(6)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(13)
        assert str(jar)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0
    assert str(jar) == ""
    
    with pytest.raises(ValueError):
        jar.withdraw(1)
        assert str(jar)


