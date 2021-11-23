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

address = cafe["location"]["address"]
zip_code = cafe["location"]["zip_code"]
city = cafe["location"]["city"]
services = cafe["categories"]

print(cafe["name"])
print(f"{address}\n{zip_code} {city}")
print()
print(cafe["website"])
print(f"Palvelut: {services[0:4]}")
