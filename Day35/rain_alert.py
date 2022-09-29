import requests
import os
from twilio.rest import Client


endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ.get('OWM_API_KEY')
account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')


params = {
    'lat': 123456,
    'lon': 1234567,
    'exclude': 'current,minutely,daily',
    'appid': api_key

}


response = requests.get(endpoint,params=params)
response.raise_for_status()

weather_data = response.json()

weather_ids = [weather_data['hourly'][num]['weather'][0]['id'] for num in range(0,12)]

def is_gonna_rain():
    for num in weather_ids:
        if num <= 700:
            return True


if is_gonna_rain():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body='Its gonna rain today.',
    from_='twilio_number',
    to='phone_number'
    )
    




    
