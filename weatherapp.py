import requests
import json
import webbrowser
city_name=input("Enter the city name :- ")
api_key=input("Provide the api key here or type 'help' for help\n")
if api_key.lower() == "help":
    print("Go to weatherapi website and get the api key to use")
    print("website link:-","www.weatherapi.com")
    webbrowser.open("https://www.weatherapi.com/")
    exit()
url=f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"
r=requests.get(url)
data=r.text
dic=json.loads(data)
print("Tracking Weather condition of :{},{},{}".format(dic["location"]["name"],dic["location"]["region"],dic["location"]["country"]))
print("Local time:",dic["location"]["localtime"])
print("Temperature in Celsius:",dic["current"]["feelslike_c"])
print("Temperature in fahrenheit:",dic["current"]["feelslike_f"])
print("UV rate:",dic["current"]["uv"])
print("Wind speed in mph:",dic["current"]["wind_mph"])
print("Wind speed in khp:",dic["current"]["wind_kph"])
print("Wind degree:",dic["current"]["wind_degree"])
print("Wind direction:",dic["current"]["wind_dir"])
print("Humidity rate:",dic["current"]["humidity"])