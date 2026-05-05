from unittest.mock import Mock

mock_location = Mock()

mock_location.move_right.return_value = 10
mock_location.move_left.return_value = 5
mock_location.move_up.return_value = 7
mock_location.move_down.return_value = 3

print(mock_location.move_right())

