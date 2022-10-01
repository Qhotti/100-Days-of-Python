import requests
import os
from twilio.rest import Client


endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ.get('OWM_API_KEY')
account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
MY_NUMBER = os.environ.get('GV_NUMBER')
LAT = os.environ.get('MY_LAT')
LNG = os.environ.get('MY_LNG')


params = {
    'lat': LAT,
    'lon': LNG,
    'exclude': 'current,minutely',
    'units': 'imperial',
    'appid': api_key

}


response = requests.get(endpoint,params=params)
response.raise_for_status()

weather_data = response.json()

min = round(weather_data['daily'][0]['temp']['min'])
max = round(weather_data['daily'][0]['temp']['max'])
uvi = round(weather_data['daily'][0]['uvi'])



weather_ids = [weather_data['hourly'][num]['weather'][0]['id'] for num in range(0,12)]

def is_gonna_rain():
    for num in weather_ids:
        if num <= 700:
            return True


if is_gonna_rain():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body=f"\n☁️\n🌧️It's gonna rain today!🌧️\nUV Index: {uvi}\nLow: {min}°F\nHigh: {max}°F",
    from_=TWILIO_NUMBER,
    to=MY_NUMBER,
    )
    




    
