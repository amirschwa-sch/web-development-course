from unittest.mock import Mock

# mock function that raises error:
# 1. create an error object - with error message
e = ValueError("Error raise by mock")
# create the mock
mock_error_function = Mock(side_effect=e)

try:
    mock_error_function()
except ValueError as e:
    print(e)

