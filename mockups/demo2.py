from unittest.mock import Mock

mock_function = Mock(side_effect=[2, 4, 6, 8])

print(mock_function())
print(mock_function())
print(mock_function())
print(mock_function())

