from unittest.mock import Mock
from unittest import TestCase
from app import weather_service

class TestWeatherService(TestCase):

    def test_get_city_name(self):
        # create a Mock object to replace the function from the api
        mock_get_weather = Mock(return_value={"city": "Haifa", "temp": 30})

        # save the original API function address
        original_function = weather_service.api.get_weather

        # set the reference to the mock function
        weather_service.api.get_weather = mock_get_weather

        try:
            # we test the service function (get_city_temp) - not the mock
            temp = weather_service.get_city_temp("Haifa")
            self.assertEqual(30, temp, "Wrong temperature value")
            # check that we actually used the mock in the test
            mock_get_weather.assert_called_with("Haifa")
        finally:
            weather_service.api.get_weather = original_function