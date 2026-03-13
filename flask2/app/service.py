# this is the application layer - business logic

# Simulation of data layer - for simplicity

weather = [
    {"city": "Tel Aviv", "temp": 17},
    {"city": "Haifa", "temp": 12},
    {"city": "Jerusalem", "temp": 10},
    {"city": "Eilat", "temp": 30},
    {"city": "Ashdod", "temp": 19},
]

# define error
class CityNotFoundError(Exception): pass


# the business function

def get_weather(city):
    for w in weather:
        if w["city"] == city:
            return w
    raise CityNotFoundError(f"Weather not found for city - {city}")

if __name__ == "__main__":
    try:
        print(get_weather(input("Enter city: ")))
    except CityNotFoundError as e:
        print(e)