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
