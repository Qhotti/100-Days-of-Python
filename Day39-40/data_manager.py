import requests
from pprint import pprint
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.get = 'https://api.sheety.co/7a396d8d2c9e3095202164ae05e4a538/flightDeals/prices'
        self.api_key = os.environ.get('SHEETY_API_KEY')
        

    def sheety_get(self):
        response = requests.get(self.get)
        json = response.json()['prices']
        return json

    def sheety_put(self,id,iata):
        sheety_header = {'Authorization': f'Bearer {self.api_key}'}
        json = {
            'price':{
            'iata code': iata}}
        
        
        sheet_id = id
        response = requests.put(url = f'https://api.sheety.co/7a396d8d2c9e3095202164ae05e4a538/flightDeals/prices/{sheet_id}',json=json,headers=sheety_header)
        print(response.text)

