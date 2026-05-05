import pytest

def login(user, password):
    return user == "admin" and password == "1234"

@pytest.fixture()
def credentials():
    print("\n -------- setup")
    return {"user": "admin", "password":"1234"}

def test1():
    assert login("admin", "1234")


def test2(credentials):
    assert login(credentials["user"], credentials["password"])

