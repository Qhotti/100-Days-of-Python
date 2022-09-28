import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}

data = requests.get('https://opentdb.com/api.php?amount=10&category=11&type=boolean', params=parameters)
data.raise_for_status()

json = data.json()

question_data = json['results']