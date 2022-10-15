import json

API_key = "9ccbbff736d86707acda287730de0c16"

lat = "46.8800"
lon = "-121.7269"

type = "hour"
start = "1662008400"
end = "1664686799"

import requests
api_url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API_key}"
response = requests.get(api_url)
json_object = response.json()
#json_object = json.loads(json_object_string)
json_object_lists = json_object['list']
print(len(json_object_lists))
day = 1
dataString = ""
# json_obj = json.loads(json_object_lists)
for hour in json_object_lists:
    date = int(day/24) + 1
    if date == 31:
        break
    if day % 24 == 0 or day==1:
        if(date <10):
            date = "0" + str(date)
        dataString += f"\nSeptember {date}, 2022\n"

    pm25 = hour["components"]["pm2_5"]
    pm10 = hour["components"]["pm10"]
    co = hour["components"]["co"]
    o3 = hour["components"]["o3"]
    dataString += f"pm2.5: {pm25}\tpm10: {pm10}\t,co: {co}\t, o3: {o3}\n"
    day += 1

print (dataString)


f = open("/Users/zach/Desktop/geoscript/airQualityAPI.txt", "w")
f.write(dataString)
f.close()


 
    

