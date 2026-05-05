# WE DONT WANT TO TEST THIS MODULE

def get_weather(city):
    print("\nCalling real weather APi...")
    return {"city": city, "temp": 25}


if __name__ == "__main__":
    print(get_weather("Tel Aviv"))
    print(get_weather("Haifa"))
    print(get_weather("Haifa")["temp"])




