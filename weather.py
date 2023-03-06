import requests

API_KEY = 'd092e5df9ff065d09085fcb9fb891d8c'
city = input('Enter location : ')
URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

response = requests.get(URL)
data = response.json()

temperature = data['main']['temp']
temperature -= 273
humidity = data['main']['humidity']
description = data['weather'][0]['description']

print(f'Temperature: {temperature} C')
print(f'Humidity: {humidity}%')
print(f'Description: {description}')
