import requests
from apiKeys import accuWeatherAPI

def fetchCurrentWeather(location_key):

    base_url = 'http://dataservice.accuweather.com/currentconditions/v1/'

    # Construct the API URL
    url = f'{base_url}{location_key}?apikey={accuWeatherAPI}'

    # Make the API request
    #response = requests.get(url)
    response = ""

    #to save the API
    return 0

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print("Current Conditions:", data[0]['WeatherText'])
        print("Temperature:", data[0]['Temperature']['Metric']['Value'], data[0]['Temperature']['Metric']['Unit'])
    else:
        print("Error:", response.status_code)

def fetchWeatherForecast(location_key):

    base_url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/'

    # Construct the API URL
    url = f'{base_url}{location_key}?apikey={accuWeatherAPI}&metric=true'

    # Make the API request
    #response = requests.get(url)
    response = ""

    #to save the API
    return 0

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print("Weather Forecast:", data['Headline']['Text'])
        print("Minimum Temperature:", data['DailyForecasts'][0]['Temperature']['Minimum']['Value'], data['DailyForecasts'][0]['Temperature']['Minimum']['Unit'])
        print("Maximum Temperature:", data['DailyForecasts'][0]['Temperature']['Maximum']['Value'], data['DailyForecasts'][0]['Temperature']['Maximum']['Unit'])
        print("Day:", data['DailyForecasts'][0]['Day']['IconPhrase'])
        print("Night:", data['DailyForecasts'][0]['Night']['IconPhrase'])
    else:
        print("Error:", response.status_code)