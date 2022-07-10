from geopy.geocoders import Nominatim
from geopy import distance
import geocoder as g
import json
import time
import requests
from requests import get

app = Nominatim(user_agent="google")

def get_location_by_address(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)

def address_by_location(latitude, longitude):
    cordinates = f"{latitude},{longitude}"
    time.sleep(1)
    try:
        return app.reverse(cordinates, language="en")
    except:
        return address_by_location(latitude, longitude)
def get_current_location():
    time.sleep(1)
    g1 = g.ip('me')
    return g1.city, g1.latlng
def current_address_by_api():
    try:

        ip = get('https://api.ipify.org').text
        url = "https://ip-location5.p.rapidapi.com/get_geo_info"
        payload = f"ip={ip}"
        headers = {
    	"content-type": "application/x-www-form-urlencoded",
    	"X-RapidAPI-Host": "ip-location5.p.rapidapi.com",
    	"X-RapidAPI-Key": "a7cf13b519msh9e34ac1bc42d3b6p162b13jsn9baf0d375985"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        json_object = json.loads(response.text)
        latitude = json_object["latitude"]
        longitude = json_object["longitude"]
        city = json_object["city"]

        return json_object
    except requests.ConnectionError as e:
        print(e)

def compare_distance(a,b):
    return distance.distance(a,b).km
