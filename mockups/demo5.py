from symtable import Class
from unittest.mock import Mock
# Car class I want to mock
class Car:

    def __init__(self):
        self.speed = 0

    def drive(self, speed):
        self.speed = speed
        return f'Car goes at {self.speed}KM/H'

    def stop(self):
        self.speed = 0
        return "Car stopped"


def drive_mock(speed):
    return f'Car Mock goes at {speed}KM/H'

car_mock = Mock(spec=Car)


car_mock.drive.side_effect = drive_mock
car_mock.stop.return_value = "Car Mock stopped"

print(car_mock.drive(150))
print(car_mock.stop())



