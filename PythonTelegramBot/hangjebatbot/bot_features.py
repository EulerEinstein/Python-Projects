import requests, json
from geopy.geocoders import Nominatim
from datetime import date
import datetime

today = date.today()

open_weather_api_key = "your_api_key"
city_name="your_city"
units = "metric" # or imperial

def getWeather():
	
	base_url = "http://api.openweathermap.org/data/2.5/forecast?"
	complete_url = base_url + "appid=" + open_weather_api_key + "&q=" + city_name + "&units=" + units
	response = requests.get(complete_url)
	x = response.json()

	if x["cod"] == "200":
		y = x["list"]
		text = "Weather: " + str(y[0]["weather"][0]["description"]) + "\n" + "Temperature: " + str(y[0]["main"]["temp"]) + " Celcius" + "\n" + "Wind speed: " + str(y[0]["wind"]["speed"]) + "km/h" + "\n\n"
		return text
	else:
		print(" City Not Found ")

def getPrayerTime():

	geolocator = Nominatim(user_agent="https://www.google.com/")
	location = geolocator.geocode(city_name, language="en")
	url = "http://api.aladhan.com/v1/calendar?" + "latitude=" + str(location.latitude) + "&longitude=" + str(location.longitude) + "&method=11" + "&month=" + today.strftime("%m") + "&year=" + today.strftime("%Y")
	response = requests.get(url)
	x = response.json()

	text = "Waktu solat\n" + "Subuh: " + x["data"][int(today.strftime("%d"))-1]["timings"]["Fajr"][0:5] + "\n" + "Zohor:" + x["data"][int(today.strftime("%d"))-1]["timings"]["Dhuhr"][0:5] + "\n" + "Asar:" + x["data"][int(today.strftime("%d"))-1]["timings"]["Asr"][0:5] + "\n" + "Maghrib:" + x["data"][int(today.strftime("%d"))-1]["timings"]["Maghrib"][0:5] + "\n" + "Isyak:" + x["data"][int(today.strftime("%d"))-1]["timings"]["Isha"][0:5] + "\n\n"
	return text

def getDate():

	return str(today.strftime("%d/%m/%Y") + "\n\n")

def getLocation():

	return "Location: " + city_name + ", "

def setLocation(location):
	global city_name
	city_name = location
	return city_name

def getStart():

	text = "Welcome to hangjebat bot! Currently this bot is still in development. However, some features are already available on this bot:\n\n"
	text = text + "1. /weather : weather info\n"
	text = text + "2. /prayertime : daily prayer time for muslim\n"
	text = text + "3. /allinfo : weather, prayer time\n"
	text = text + "4. /changeLocationTo (city name): change location\n"

	return text

def getCommands():
	return "Available commands: /start, /weather, /prayertime, /allinfo"


