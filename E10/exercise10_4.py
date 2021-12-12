import json

# .json listamuotoon:
countries_handle = open("countries.json", "r")
countries_content = countries_handle.read()
countries_list = json.loads(countries_content)

print("Kaikki maat ja pääkaupungit:")

# tulostetaan maat ja pääkaupungit
for index in countries_list:
    print(f" {index['country']}: {index['capital']}")

countries_handle.close()