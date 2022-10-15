import requests
from bs4 import BeautifulSoup

url = "https://www.iqair.com/us/usa/washington/rainier"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")



#grab pm2.5 data 
pmData = "pm2.5: "
for val in soup.find_all('span'):
    if(val.parent.name == "td"):
        if("cdk-describedby" in str(val)):
            # print(val.text[0:len(val.text)-1] + " µg/m³")
            pmData += val.text[0:len(val.text)-1] + " µg/m³"

#Grab temperature and humidity 
weather = ""
readNextValue = False
for val2 in soup.find_all('td'):
    comma = True
    if readNextValue:
        # print(val2.text)
        txt = val2.text
        if("°C" in val2.text):
            txt = val2.text.replace("°C", "°F")
        elif("%" in val2.text):
            txt += " Humidity"
            comma = False
        if comma:
            weather += txt + ", "
        else:
            weather += txt
        readNextValue = False
    if "Weather" in val2 or "Temperature" in val2 or "Humidity" in val2:
        readNextValue = True
    
    
    
#find ozone 
url = "https://air.plumelabs.com/air-quality-in-mount-rainier-national-park-aw-29215_poi"
#accuweather requires User-Agent Header for GET requests
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"}
result = requests.get(url)
soup2 = BeautifulSoup(result.content, "html.parser")
ozone = "O3: "
for val3 in soup2.find_all("li"):
    if("pollutant-column" in str(val3) and "O3" in str(val3) and "upm" in str(val3)):
        ozone += val3.text[1:5] + " AQI"

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
time = now.strftime("%m/%d/%Y %H:%M:%S")
# print("date and time =", time)

output = time + " \t" + pmData + " \t" + ozone + " \t" + weather + " \n"

f = open("/Users/zach/Desktop/geoscript/airQuality.txt", "a")
f.write(output)
f.close()

