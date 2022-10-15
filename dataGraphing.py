import matplotlib.pyplot as plt
import numpy as np


def weatherForDate(weather, day):
    hourlyTemp = []
    hourlyWeather = []
    hourlyHumidity = []
    hourlyVisibility = []
    
    for line in range(0, len(weather)):
        if(f"September {day}" in weather[line]):
            #Print Date
            #print(weather[line])
            for hour in range(1, 24):
                #Print data
                dataLine = weather[line + hour]
                #Parse Temperature
                tempEndIndex = dataLine.index('\t')
                temp = dataLine[6:tempEndIndex-2]
                hourlyTemp.append(float(temp))
                #Parse Weather
                weatherEndIndex = dataLine.index('\t', tempEndIndex+1)
                weatherData = dataLine[tempEndIndex+11:weatherEndIndex]
                hourlyWeather.append(weatherData)
                #Parse Humidity
                humidityEndIndex = dataLine.index('\t', weatherEndIndex + 1)
                humidity = dataLine[weatherEndIndex+12:humidityEndIndex]
                hourlyHumidity.append(float(humidity))
                visibility = dataLine[humidityEndIndex+14:]
                hourlyVisibility.append(visibility)

    return hourlyTemp, hourlyWeather, hourlyHumidity, hourlyVisibility
                
def PollutantForDate(airQuality, day):
    hourlypm25 = []
    hourlypm10 = []
    hourlyco = []
    hourlyo3 = []
    for line in range(0, len(airQuality)):
        if(f"September {day}" in airQuality[line]):
            #Print Date
            for hour in range(1, 24):
                #Print data
                dataLine = airQuality[line + hour]
                #Parse pm2.5
                pm25Index = dataLine.index('\t')
                pm25 = dataLine[7:pm25Index]
                hourlypm25.append(float(pm25))

                pm10Index = dataLine.index('\t', pm25Index+1)
                pm10 = dataLine[pm25Index+7:pm10Index]
                hourlypm10.append(pm10)

                coIndex = dataLine.index('\t', pm10Index+1)
                co = dataLine[pm10Index+6:coIndex]
                hourlyco.append(co)

                o3 = dataLine[coIndex+7:]
                hourlyo3.append(float(o3))

    return hourlypm25, hourlypm10, hourlyco, hourlyo3
        


class Date:
    def __init__(self, temp, weather, humidity, visibility, pm25, pm10, co, o3):
        self.temp = temp
        self.weather = weather
        self.humidity = humidity
        self.visibility = visibility
        
        self.pm25 = pm25
        self.pm10 = pm10
        self.co = co
        self.o3 = o3
    def get_temp(self):
        return self.temp
    def get_weather(self):
        return self.weather
    def get_humidity(self):
        return self.humidity
    def get_visibility(self):
        return self.visibility
    def get_pm25(self):
        return self.pm25
    def get_pm10(self):
        return self.pm10
    def get_co(self):
        return self.co
    def get_o3(self):
        return self.o3
    


weather = ""
airQuality = ""
with open('weatherAPI.txt') as f:
    weather = f.readlines()
    
    with open('airQualityAPI.txt') as g:
        airQuality = g.readlines()


days = []
for day in range(1,31):
    if(day < 10):
        day = "0" + str(day)
    hourlyTemp, hourlyWeather, hourlyHumidity, hourlyVisibility = weatherForDate(weather, day)
    hourlypm25, hourlypm10, hourlyco, hourlyo3 = PollutantForDate(airQuality, day)
    days.append(Date(hourlyTemp, hourlyWeather, hourlyHumidity, hourlyVisibility, hourlypm25, hourlypm10, hourlyco, hourlyo3))


figure, axis = plt.subplots(2, 2)

v = days[0].get_o3()
w = days[0].get_humidity()
y = days[0].get_temp()
z = days[0].get_pm25()

x = [i for i in range(1,24)]

axis[0,0].plot(x,y)
axis[0,0].set_xlabel('Hour')
axis[0,0].set_ylabel('Temperature °F')
axis[0, 0].set_title("Temperature")

axis[0,1].plot(x,z)
axis[0,1].set_xlabel('Hour')
axis[0,1].set_ylabel('Pm2.5 µg/m³')
axis[0, 1].set_title("Pm2.5 Concentration")

axis[1,0].plot(x,w)
axis[1,0].set_xlabel('Hour')
axis[1,0].set_ylabel('% Humidity')
axis[1, 0].set_title("Humidity")

axis[1,1].plot(x,v)
axis[1,1].set_xlabel('Hour')
axis[1,1].set_ylabel('o3 µg/m³')
axis[1,1].set_title("o3")


plt.show()
