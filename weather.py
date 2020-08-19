import requests
from geopy.geocoders import Nominatim

# openweathermap api key
api_key = 'Super secret'

geolocator = Nominatim(user_agent='weather.py')
location = geolocator.geocode("Olympus Mons")
lat, lon = location.latitude, location.longitude

html = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}"

result = requests.get(html)
data = result.content
print(data)
