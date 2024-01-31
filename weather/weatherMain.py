import settings
import re
from weather.fetchLocationKey import searchLocationKey
from weather.fetchWeatherData import fetchCurrentWeather, fetchWeatherForecast

def weatherPreProcess(context):
    if(context.find("tomorrow") != -1 or context.find("forecast") != -1):
        weatherForecast(context)
    else:
        currentWeather(context)


def currentWeather(context):
    if(context.find(" in ") == -1 and context.find(" for ") == -1):
        settingsCityCurrentWeather()


    else:
        otherCityCurrentWeather(context)

def weatherForecast(context):

    if(re.search('for tomorrow for (\w+)', context)):
        otherCityWeatherForecast(context)
    elif(re.search('for (\w+) for tomorrow', context)):
        otherCityWeatherForecast(context)
    elif(re.search('for tomorrow in (\w+)', context)):
        otherCityWeatherForecast(context)
    elif(re.search('in (\w+) for tomorrow', context)):
        otherCityWeatherForecast(context)
    elif(re.search('forecast for (\w+)', context)):
        otherCityWeatherForecast(context)
    elif(re.search('forecast in (\w+)', context)):
        otherCityWeatherForecast(context)
    elif(re.search('in (\w+) forecast', context)):
        otherCityWeatherForecast(context)
    elif(re.search('for (\w+) forecast', context)):
        otherCityWeatherForecast(context)
    elif(re.search('in (\w+) tomorrow', context)):
        otherCityWeatherForecast(context)
    elif(re.search('for (\w+) tomorrow', context)):
        otherCityWeatherForecast(context)
    elif(re.search('tomorrow in (\w+)', context)):
        otherCityWeatherForecast(context)
    elif(re.search('tomorrow for (\w+)', context)):
        otherCityWeatherForecast(context)

    else:
        settingsCityWeatherForecast()


def settingsCityCurrentWeather():
    print('SC City:'+  settings.city)
    fetchCurrentWeather(searchLocationKey(settings.city))

def settingsCityWeatherForecast():
    print('SF City:'+  settings.city)
    fetchWeatherForecast(searchLocationKey(settings.city))


def otherCityCurrentWeather(context):
    city = ""
    if(re.search('in (\w+)', context)):
        instruction = context.split(" in ")
        city = instruction[1]

    elif(re.search('for (\w+)', context)):
        instruction = context.split(" for ")
        city = instruction[1]
    
    print('C City:'+  city)
    fetchCurrentWeather(searchLocationKey(city))

def otherCityWeatherForecast(context):
    city = ""
    patterns = [
            (r'for tomorrow for (\w+)', " for tomorrow for "),
            (r'for (\w+) for tomorrow', " for "),
            (r'for tomorrow in (\w+)', " for tomorrow in "),
            (r'in (\w+) for tomorrow', " in "),
            (r'forecast for (\w+)', " forecast for "),
            (r'forecast in (\w+)', " forecast in "),
            (r'in (\w+) forecast', " in "),
            (r'for (\w+) forecast', " for "),
            (r'in (\w+) tomorrow', " in "),
            (r'for (\w+) tomorrow', " for "),
            (r'tomorrow in (\w+)', " tomorrow in "),
            (r'tomorrow for (\w+)', " tomorrow for "),
        ]

    for pattern, separator in patterns:
        instruction = extract_city(context, pattern)
        if instruction:
            city = instruction
            break

    if(re.search('tomorrow', city)):
        city = city.split(" tomorrow")[0]

    print('F City:'+  city)
    fetchWeatherForecast(searchLocationKey(city))

def extract_city(context, pattern):
    match = re.search(pattern, context)
    if match:
        instruction = match.group(1)
        return instruction
    return None