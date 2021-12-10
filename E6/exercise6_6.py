# lista
basket = [
    "omena",
    "banaani",
    "kirsikka",
    "porkkana",
    "peruna",
    "tomaatti",
    "kaali"
]

# pyydetään poistettava sana
query = input("Syötä sana:\n")

# tarkistetaan if-lauseella onko kyseinen str listalla
if query in basket:
    # jos on, poistetaan
    basket.remove(query)

    # ja tulostetaan silmukalla
    for item in basket:
        print(item)
else:
    print("Valittua sanaa ei löytynyt.")

# jos query on numero, tämä if-lause nappaa sen
if query.isnumeric():
    # muutetaan kokonaisluvuksi
    query = int(query)
    #query = query + 1
    del basket[query-1]

    # ja tulostetaan silmukalla
    for item in basket:
        print(item)
