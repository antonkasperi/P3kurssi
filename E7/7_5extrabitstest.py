import json
import urllib.request
#import var_dump as vd

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

windspeeds = [x['wind'] for x in weather]
corresponding_index_windiest = windspeeds.index(max(windspeeds))
corresponding_index_leastwindy = windspeeds.index(min(windspeeds))

print(f"Tänään eniten tuulee sijainnissa: {weather[corresponding_index_windiest]['location']}, {max(windspeeds)} m/s")
print(f"Tänään vähiten tuulee sijainnissa: {weather[corresponding_index_leastwindy]['location']}, {min(windspeeds)} m/s")
print()
#vd.var_dump(weather)
wind_lapland = []
wind_middle = []
wind_south = []

for x in weather:
    if x['area'] == 'lapland':
        wind_lapland.append(x['wind'])
    elif x['area'] == 'middle':
        wind_middle.append(x['wind'])
    elif x['area'] == 'south':
        wind_south.append(x['wind'])

total_lapland = 0
total_middle = 0
total_south = 0
for speed in wind_lapland:
    total_lapland = total_lapland + speed
    avgspeed_lapland = total_lapland / len(wind_lapland)
    avgspeed_lapland = round(avgspeed_lapland, 2)

for speed in wind_middle:
    total_middle = total_middle + speed
    avgspeed_middle = total_middle / len(wind_middle)
    avgspeed_middle = round(avgspeed_middle, 2)

for speed in wind_south:
    total_south = total_south + speed
    avgspeed_south = total_south / len(wind_south)
    avgspeed_south = round(avgspeed_south, 2)

print(f"Keskimääräinen tuuli, Lappi: {avgspeed_lapland} m/s")
print(f"Keskimääräinen tuuli, Maan keskiosa: {avgspeed_middle} m/s")
print(f"Keskimääräinen tuuli, Etelä-Suomi: {avgspeed_south} m/s")
