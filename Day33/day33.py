import math
import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 10
MY_LNG = 10                                     # Fill in your own details
EMAIL = 'blank'
PASSWORD = 'blank'


def is_overhead():
    api_request = requests.get(url = 'http://api.open-notify.org/iss-now.json')
    api_request.raise_for_status
    data = api_request.json()
    longitude = float(data['iss_position']['longitude'])                                     #Current ISS Location
    latitude = float(data['iss_position']['latitude'])
    if math.isclose(MY_LAT,latitude,abs_tol=5) == True and math.isclose(MY_LNG,longitude,abs_tol=5) == True:
        return True
    else:
        return False



def is_dark():
    
    parameters={'formatted':0}
    
    response = requests.get('https://api.sunrise-sunset.org/json',params= parameters)
    response.raise_for_status()
    json = response.json()
    # print(json)
    sunrise = int(json['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(json['results']['sunset'].split('T')[1].split(':')[0])
    # print(sunrise)

    time_now = datetime.now()
    current_hour = time_now.hour
    
    if current_hour >= sunset or current_hour <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if is_dark() and is_overhead():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL, 
                to_addrs=EMAIL,
                msg='Subject:ISS Location\n\nLook up! The ISS should be right above you!')