# test for equality
import random

import pytest


def test_equality():
    assert 2 + 2 == 4

def test_is_true():
    is_logged_in = True
    assert is_logged_in

def test_numeral_proximity():
    a = 0.1
    b = 0.2
    total = a + b
    assert total == pytest.approx(0.3)

def test_member_of():
    user_name = "Oren"
    names = ["Dan", "Ran", "Liat", "Oren", "Danna"]
    assert user_name in names

def test_number_member_of():
    numbers = (2, 4, 6, 8)
    r = random.randint(0, 10)
    assert r in numbers


def rnd() -> int:
    r = random.randint(0, 10)
    return r

# test for the right type
def test_rnd_returns_int():
    x = rnd()
    assert isinstance(x, int)

def divide(a, b):
    return a / b

def test_divide_negative():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_negative_error_access():
    with pytest.raises(ZeroDivisionError) as context:
        divide(10, 0)
    e = context.value
    error_message = str(e)
    assert error_message in "division by zero"



