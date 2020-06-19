import requests
WEATHERAPI = '******' #Put Your API Key Here
def getquote():
	url = 'https://api.quotable.io/random'
	headers = {}
	response = requests.get(url, headers=headers)
	quote=response.json()['content']
	return quote

def getcoronaupdates():
	url = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code=IN'
	headers = {}
	response = requests.get(url, headers=headers)
	confirmed = response.json()['latest']['confirmed']
	deaths = response.json()['latest']['deaths']
	last_updated = response.json()['locations'][0]['last_updated']
	Country = response.json()['locations'][0]['country']
	last_updated_date = last_updated[:10]
	last_updated_time = last_updated[11:16];
	return "Latest Data updated on " + str(last_updated_date) + " at " + str(last_updated_time) + " from Worldwide Data repository " + '\n' +  "Country : " + str(Country) + '\n' + "Confirmed : " + str(confirmed) + '\n' + "Deaths : " + str(deaths)

def weather(location):
	url = 'https://api.openweathermap.org/data/2.5/weather?q=' + str(location) + '&units=metric&appid=' + str(WEATHERAPI)
	headers = {}
	response = requests.get(url, headers=headers).json()
	description = response['weather'][0]['description']
	current_temp = response['main']['temp']
	temp_min = response['main']['temp_min']
	temp_max = response['main']['temp_max']
	pressure = response['main']['pressure']
	humidity = response['main']['humidity']
	wind_speed = response['wind']['speed']
	return "Location: " + str(location) + '\n' + "Description :" + str(description) + '\n' + "Current Temp : " + str(current_temp) +  '\n' + "Pressure :" + str(pressure) + '\n' + "Humidity :" + str(humidity) + '\n' "Wind Speed :" + str(wind_speed) + '\n'





