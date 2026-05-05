# WE DO WANT TO TEST THIS MODULE

import app.weather_api_client as api

def get_city_temp(city):
    data = api.get_weather(city)
    return data["temp"]

if __name__ == "__main__":
     print(get_city_temp("Jerusalem"))

