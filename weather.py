import requests
api_key = '8bc6c1d48afde5015eeeb852387450fd'

city = input('Enter city name: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    temp1 = temp - 273.15
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp1} C')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
