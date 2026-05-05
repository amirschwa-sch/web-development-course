from unittest.mock import Mock

def add(a, b):
    return a + b

add_mock = Mock(side_effect=add)

x = add_mock(2, 7)
print(x)

print(add_mock(100, 200))
print(add_mock(2, 9))
print(add_mock(10, 20))

print("=================")
def get_max(a, b):
    if a > b:
        return a
    else:
        return b

mock_max = Mock(side_effect=get_max)

print(mock_max(3, 7))
print(mock_max(10, 2))

