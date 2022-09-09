import requests

import api_key as key
import getgps
import opmaak
import weerOmschrijving


def weeropvragen():  ##the weather conditions will be gathered right here
    linkinfo = getgps.coords()
    CITY = getgps.coordscityname()
    api = key.key()  ##Fill in your api key from openweather here
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    taal = '&lang=EN'
    complete_url = base_url + "appid=" + api + "&q=" + linkinfo + taal
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    huidige_temperatuur = y["temp"]
    temperatuur = str(round(huidige_temperatuur - 273.15))
    z = x["weather"]
    omschrijving = str(z[0]["description"])
    icon = weerOmschrijving.icon(omschrijving, temperatuur)
    opmaak.tekst(temperatuur, CITY, icon)


def icon(omschrijving,
         temperatuur):  ##Here the description will be added to the current weather conditions and also the icons
    if omschrijving == 'clear sky':
        icon = ''
        omschrijving = 'De lucht is vrij'
        if temperatuur <= '20':
            tip = '\nHet is wat aan de frisse kant'
        elif temperatuur >= '30':
            tip = '\nHittegolf kijk op https://www.knmi.nl/home voor actuele weer codes'
        else:
            tip = '\nHet is lekker warm weer'
    elif omschrijving == 'few clouds':
        icon = '☁️'
        omschrijving = 'Het is licht bewolkt'
        if temperatuur <= '20':
            tip = '\nHet is wat aan de frisse kant'
        elif temperatuur >= '30':
            tip = '\nHittegolf kijk op https://www.knmi.nl/home voor actuele weer codes'

        else:
            tip = '\nHet is lekker warm weer'
    elif omschrijving == 'scattered clouds':
        icon = '🌤️'
        weather_description = 'Het is bewolkt'
        if temperatuur <= '20':
            tip = '\nHet is wat aan de frisse kant'
        elif temperatuur >= '30':
            tip = '\nHittegolf kijk op https://www.knmi.nl/home voor actuele weer codes'

        else:
            tip = '\nHet is lekker warm weer'
    elif omschrijving == 'broken clouds' or 'overcast clouds':
        icon = '🌤'
        omschrijving = 'De lucht heeft opengebroken wolken'
        if temperatuur <= '20':
            tip = '\nHet is wat aan de frisse kant'
        elif temperatuur >= '30':
            tip = '\nHittegolf kijk op https://www.knmi.nl/home voor actuele weer codes'

        else:
            tip = '\nHet is lekker warm weer'
    elif omschrijving == 'shower rain':
        icon = '🌧️🌧️'
        omschrijving = 'Het stortregend \n Tip: Ik zou naar binnen gaan'
    elif omschrijving == 'rain' or 'light rain' or 'moderate rain' or 'heavy intensity rain' or 'very heavy rain' or 'extreme rain' or 'freezing rain' or '	light intensity shower rain' or 'heavy intensity shower rain' or 'ragged shower rain':
        icon = '🌦️'
        omschrijving = 'Het regent'
    elif omschrijving == 'thunderstorm':
        icon = '⛈️'
        omschrijving = 'Het onweert'
    elif omschrijving == 'snow' or 'light snow' or 'Heave snow' or 'Sleet' or 'Light shower sleet' or 'Shower sleet' or 'Light rain and snow' or 'Rain and snow' or 'Light shower snow' or 'Shower snow' or 'Heavy shower snow':
        icon = '🌨️'
        omschrijving = 'Het sneeuwt'
        if temperatuur <= '2':
            tip = 'Het kan glad zijn'
        else:
            tip = 'kijk op https://www.knmi.nl/home voor actuele weer codes'
    elif omschrijving == 'mist' or 'Smoke' or 'Haze' or 'sand/ dust whirls' or 'fog' or 'sand' or 'dust' or 'volcanic ash' or 'squalls':
        icon = '🌫️'
        omschrijving = 'Het sneeuwt'
    elif omschrijving == 'Tornado':
        icon = '🌪️'
        omschrijving = 'Er is een Tornado ga naar binnen'

    else:
        icon = ''
        omschrijving = 'Drizzle'
        icon = str(icon)
    return omschrijving + icon + tip
