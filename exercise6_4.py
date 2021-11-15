# ao lista
products = ["T1565_2020", "T2432_2019",
            "T8551_2018", "T3345_2019",
            "Y51372_2019", "Y76715_2017",
            "E98144_2018", "T7733_2020",
            "E7614_2021", "E9722_2017",
            "Y89875_2020", "T61287_2021",
            "E9152_2019", "T7749_2021"]

# kysytään minkä vuoden koodit halutaan nähdä
# tämä tarkoituksella str että voidaan hakea sitä käyttäen
query = input("Minkä vuoden koodit haetaan?\n")

# luodaan tyhjä lista tilauksille, joissa on oikea koodi
matches = []

# silmukoidaan koko products-lista läpi, haetaan tiettyä substringiä (query)
for order in products:
    if query in order:
        # jos löytyy, lisätään matches-listaan
        matches.append(order)

# toinen tyhjä lista, johon kerätään pelkät tuotekoodit
printables = []

# silmukoidaan ja .split alaviivan kohdalta, lisätään printattavat-listaan
for stuff in matches:
    stuff = stuff.split("_")
    printables.append(stuff[0])

# lopuksi tulostetaan tuotekoodit
for p in printables:
    print(p)