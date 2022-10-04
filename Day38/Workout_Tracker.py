import requests
import datetime as dt
import os

APP_ID = '018f9ce8'
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')
GENDER = 'MALE'
WEIGHT_KG = 50
HEIGHT_CM = 160
AGE = 19

today = dt.datetime.now()
time = today.strftime("%I:%M:%S %p")
current_date = today.strftime('%d/%m/%Y')


nutrition_end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'

sheety_retrieve_endpoint = 'https://api.sheety.co/7a396d8d2c9e3095202164ae05e4a538/myWorkouts/workouts'

sheety_post_endpoint = 'https://api.sheety.co/7a396d8d2c9e3095202164ae05e4a538/myWorkouts/workouts'


query = input('What exercise did you do today? ')

nut_headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
nut_params = {
    'query': query,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
    
}

sheety_header = {
    'Authorization': f'Bearer {SHEETY_API_KEY}'
}

sheety_get = requests.get(sheety_retrieve_endpoint)








nut_response = requests.post(url = nutrition_end_point,json = nut_params, headers=nut_headers)

nut_json = nut_response.json()['exercises']

# print(nut_json)

for workout in nut_json:
    exercise = workout['name'].title()
    duration = workout['duration_min']
    calories = round(workout['nf_calories'])
    
    if duration < 60:
        t = duration
        duration =f'{t} minutes'
    
    elif duration < 120:
        t = duration / 60
        duration =f'{t} hour'
    elif duration >= 120:
        t = duration / 60
        duration =f'{t} hours'    
    
    
    sheety_json = {
        'workout':{
            'date': current_date,
            'time': time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories,
        }
    }

    sheety_response = requests.post(url = sheety_post_endpoint,json=sheety_json,headers=sheety_header)

    t = sheety_response.json()

print('done')