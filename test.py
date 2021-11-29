import json
import urllib.request
import var_dump as vd

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

windspeeds = [x['wind'] for x in weather]
corresponding_index_windiest = windspeeds.index(max(windspeeds))
corresponding_index_leastwindy = windspeeds.index(min(windspeeds))

print(f"Tänään eniten tuulee sijainnissa: {weather[corresponding_index_windiest]['location']}, {max(windspeeds)} m/s")
print(f"Tänään vähiten tuulee sijainnissa: {weather[corresponding_index_leastwindy]['location']}, {min(windspeeds)} m/s")

vd.var_dump(weather)
wind_lapland = []
wind_middle = []
wind_south = []

for place in weather:
    if 'area' == "lapland":
        wind_lapland.append(place['wind'])
    elif 'area' == "middle":
        wind_middle.append(place['wind'])
    elif 'area' == "south":
        wind_south.append(place['wind'])

print(wind_lapland)
