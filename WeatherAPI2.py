import requests
import json
#get weather data
day = "01"
writeText = ""
for i in range(1, 31):
    if (i < 10):
        day = f"0{i}"
    else:
        day = str(i)
    writeText += f"September {day}, 2022\n"
    url = f"http://api.weatherapi.com/v1/history.json?key=5c57fa95f1e04a37b6d194106221310&q=98304&dt=2022-09-{day}"
    response = requests.get(url)
    json_object = response.json()
    for hour in range(1, 24):
        humidity = json_object['forecast']['forecastday'][0]['hour'][hour]['humidity']
        time = json_object['forecast']['forecastday'][0]['hour'][hour]['time']
        visibility = json_object['forecast']['forecastday'][0]['hour'][hour]['vis_miles']
        temp = json_object['forecast']['forecastday'][0]['hour'][hour]['temp_f']
        weather = json_object['forecast']['forecastday'][0]['hour'][hour]['condition']['text']
        writeText+= f"Temp: {temp}°F\t Weather: {weather}\t Humidity: {humidity}\t Visibility: {visibility}\n"
    writeText+="\n"

print(writeText)
f = open("/Users/zach/Desktop/geoscript/weatherAPI.txt", "a")

f.write(writeText)
f.close()