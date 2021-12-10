import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

# using list comprehension to make a list of the wind speeds
windspeeds = [x['wind'] for x in weather]

# creating variables for the location names based on the max/min values
corresponding_index_windiest = windspeeds.index(max(windspeeds))
corresponding_index_leastwindy = windspeeds.index(min(windspeeds))

# printing the results by using the index-denoting variable to get the place name
# and the max/min values to get the float values
print(f"Tänään eniten tuulee sijainnissa: {weather[corresponding_index_windiest]['location']}, {max(windspeeds)} m/s")
print(f"Tänään vähiten tuulee sijainnissa: {weather[corresponding_index_leastwindy]['location']}, {min(windspeeds)} m/s")
print()

# lists for the separate wind speed values
wind_lapland = []
wind_middle = []
wind_south = []

# extraxting the wind speed values and assigning them into correct lists
for x in weather:
    if x['area'] == 'lapland':
        wind_lapland.append(x['wind'])
    elif x['area'] == 'middle':
        wind_middle.append(x['wind'])
    elif x['area'] == 'south':
        wind_south.append(x['wind'])

# defining the values for totals
total_lapland = 0
total_middle = 0
total_south = 0

# in a for-loop calculating the average wind speed for each area, rounding the result as requested
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

# printing the results
print(f"Keskimääräinen tuuli, Lappi: {avgspeed_lapland} m/s")
print(f"Keskimääräinen tuuli, Maan keskiosa: {avgspeed_middle} m/s")
print(f"Keskimääräinen tuuli, Etelä-Suomi: {avgspeed_south} m/s")
