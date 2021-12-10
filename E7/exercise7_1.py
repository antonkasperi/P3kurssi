# luodaan dict
cafe = {
        "name": "Imaginary Cafe Oy",
        "website": "https://edu.frostbit.fi/sites/cafe/",
        "categories": [
            "cafe",
            "tea",
            "lunch",
            "breakfast"
        ],
        "location": {
            "city": "Rovaniemi",
            "address": "Testikuja 22",
            "zip_code": "96200"
        }
    }

# tulostetaan pyydetyt tiedot
print(cafe["name"])
print(f"{cafe['location']['address']}\n{cafe['location']['zip_code']} {cafe['location']['city']}")
print()
print(cafe['website'])

# tässä kohtaa jouduin hieman googlailemaan kunnes löysin .join() metodin
# jotta saan listan tulostettua f-stringin kanssa ja ilman hakasulkeita
services = []
for service in cafe['categories']:
    services.append(service)

separator = ", "
print(f'Palvelut: {separator.join(services)}')

# löytämäni esimerkin koodi näytti tältä, mutta yksinkertaistin sitä koska
# rehellisesti sanottuna en ymmärrä miksi tuolla on for-toistolause :)
# varmasti olisi myös tapa tehdä tämä suoraan cafe-dictistä ja ilman erillistä
# "services"-listan luomista
# print(f'Palvelut: {", ".join(str(x) for x in services)}')
