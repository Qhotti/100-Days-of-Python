import requests
import datetime as dt

TOKEN = 'jnsdfjlkasdpiowrgnow44783'
USERNAME = 'qhotti'
GRAPH_ID = 'graph1'

today = dt.datetime.now()
current_date = today.strftime('%Y%m%d')

pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
pixel_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}'





params={
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
    
}

graph_params ={
    'id': 'graph1',
    'name': 'Reading Graph',
    'unit': 'chapters',
    'type': 'int',
    'color': 'shibafu',
}

headers = {
    'X-USER-TOKEN': 'jnsdfjlkasdpiowrgnow44783'
}




choice = input('Would you like to: add, update, or remove a pixel?\n').lower()

if choice == 'add':
    quantity = input('How many chapters did you read today?:\n')
    pixel_params = {'date': current_date,'quantity': quantity,}
    pixel_response = requests.post(url = pixel_endpoint, json=pixel_params, headers=headers)
    print(pixel_response.text)
elif choice == 'update':
    date = input('What is the date of the pixel? format: yyyyMMdd\n')
    pixel_update_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date}'
    update_quantity = input('How many chapters did you actually read?:\n')
    update_params = {'quantity': update_quantity,}
    pixel_response = requests.put(url = pixel_update_endpoint, json=update_params, headers=headers)
    print(pixel_response.text)
elif choice == 'remove':
    date = input('What is the date of the pixel you want to remove? format: yyyyMMdd\n')
    pixel_update_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{date}'
    pixel_response = requests.delete(url = pixel_update_endpoint,headers=headers)
    print(pixel_response.text)


