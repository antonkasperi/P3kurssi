import urllib.request
import json
import var_dump as vd

# get internet data
url = 'https://edu.frostbit.fi/api/events'
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# tarvittava data on nyt data-muuttujassa!
data = json.loads(raw_data)
#vd.var_dump(data)

first_event = data[0]
#vd.var_dump(first_event)

choice = input("Millaisia tapahtumia haet?\n")


for event in data:
    address = event['address']
    address_text = f"{address['postal_code']} {address['street_address']}"

    categories = ", ".join(event['categories'])

    if choice not in categories:
        continue

    print(event['name'])
    print(address_text)

    if categories != "":
        print(categories)
        print()
    else:
        print("Ei kategorioita.")