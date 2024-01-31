import requests
from apiKeys import accuWeatherAPI

def searchLocationKey(city_name):

    base_url = 'http://dataservice.accuweather.com/locations/v1/cities/search'

    # Construct the API URL
    url = f'{base_url}?apikey={accuWeatherAPI}&q={city_name}'

    # Make the API request
    #response = requests.get(url)
    response = ""

    #to save the API
    return 0

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Extract the location key from the response
        if data:
            location_key = data[0]['Key']
            return location_key
        else:
            print("Location not found.")
            return -2
    else:
        print("Error:", response.status_code)
        return -1
