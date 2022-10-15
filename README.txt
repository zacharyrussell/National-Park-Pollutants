airIndices.py can be ran to collect current weather and pollutant data from Mount Rainier.
URL should be changed if another location is measured. 
Results are appended to ./airQuality.txt after completion

WeatherAPI.py pulls pollutant data (PM2.5, o3, PM10, co) using OpenWeather's API for every hour 
of every day in September 2022.
Results are written to ./airQualityAPI.txt

WeatherAPI2.py pulls WEATHER data (conditions, temperature, humidity, visibility) using 
weatherAPI's API for every hour of every day in September 2022. 
Results are written to ./weatherAPI.txt

dataGraphing.py parses and creates visualizations of collected data on specified days, or averages
across the whole month.
