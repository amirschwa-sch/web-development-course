import pytest

@pytest.fixture
def simple():
    print("\n----------------Setup - runs before the test function")
    yield
    print("\n----------------Teardown - runs after the test function")




def test1(simple):
    print("\n==test1")
    assert 1 == 1


def test2(simple):
    print("\n==test2")
    assert 1 == 1

