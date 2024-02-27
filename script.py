import requests

def fetch_weather_data():
    url = f'http://api.weather.gov/stations'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch the weather data. Status code: {response.status_code}')
        return None

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    print(weather_data)


