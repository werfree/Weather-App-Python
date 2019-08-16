import requests

api_key = "9234260331cc0d922948f6bfccbc76df"
base_url = r"http://api.openweathermap.org/data/2.5/weather?"
city = input("Enter City Name = ")
comp_url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(comp_url)
j = response.json()

# read Json
if j["cod"] != "404":
    y = j["main"]
    temp = round(int(y["temp"])-273.15,2)
    pressure = y["pressure"]
    humidity = y["humidity"]
    weather = j["weather"]
    weather_d = weather[0]["main"]

    print(" Temperature (in Celsius unit) = " +
                    str(temp) +
          "\n Atmospheric pressure (in hPa unit) = " +
                    str(pressure) +
          "\n Humidity (in percentage) = " +
                    str(humidity) +
          "\n Weather = " +
                    str(weather_d))
else:
    print("Enter a valid City or Check the Internet Connection")
