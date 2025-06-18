import requests

url = 'https://pokeapi.co/api/v2/pokemon/1'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    with open('response.json', 'w') as json:
        json.write(str(data))
else:
    print('Invalid status code')