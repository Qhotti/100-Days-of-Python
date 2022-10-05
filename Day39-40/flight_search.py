import requests
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
        
    def iata(self,city):
        header = {
            'apikey': 'QAfS8CNt_aP-gNS4nqQKtd1MdYiUI5MZ'
        }
        param = {
            'term': city,
            'location_types':'city',
        }
        response = requests.get(url = 'https://tequila-api.kiwi.com/locations/query', params=param, headers=header )
        json = response.json()
        return json['locations'][0]['code']