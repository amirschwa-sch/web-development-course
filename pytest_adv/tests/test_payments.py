import pytest

@pytest.mark.functional
def test1_authentication_positive():
    a = 2
    b = 3
    assert a + b == 5

@pytest.mark.functional
def test1_authentication_negative():
    a = 2
    b = 3
    assert a + b == 5

@pytest.mark.functional
def test_authorization_positive():
    a = 2
    b = 3
    assert a + b == 5

@pytest.mark.functional
def test_authorization_negative():
    a = 2
    b = 3
    assert a + b == 5

@pytest.mark.performance
def test_performance():
    a = 2
    b = 3
    assert a + b == 5

