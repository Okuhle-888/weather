import requests 
from pprint import pprint

API_KEY = '7e3b2d4403033944434eed732b805ba2'

city = input('insert name of the City: ')

sending_response = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY+'&q='+city

weather_data = requests.get(sending_response).json()

pprint(weather_data)  #printing the data in pretty print