# This is about geo-localization & sys info from pc to use it for data for checking weather in region of this pc
# geocoder is installed with pip
import requests
import socket

h_name = socket.gethostname()
IP_address = socket.gethostbyname(h_name)
print("hostname =" + h_name)
print("my ip is:" + IP_address)




url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Mountain View, CA'}
r = requests.get(url, params=params)
results = r.json()['results']
location = results[0]['geometry']['location']
print(location['lat'], location['lng'])