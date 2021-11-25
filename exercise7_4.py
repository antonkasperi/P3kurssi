import var_dump as vd
movies = [
    {"name": "Komisario Palmun erehdys", "year": 1960},
    {"name": "Kauas pilvet karkaavat", "year": 1996},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Pidä huivista kiinni, Tatjana", "year": 1994},
    {"name": "Vares - Keltainen leski", "year": 2004},
    {"name": "Milk", "year": 2008},
]

new_movies = []
old_movies = []

#vd.var_dump(movies)

for movie in movies:
    for year in range(movie['year']):
        if year < 2000:
            old_movies.append(movie['name'])
            break

        elif year > 2000:
            new_movies.append(movie['name'])
            break

print('Seuraavat elokuvat on julkaistu 2000-luvulla:')
for movie in new_movies:
    print(movie)
print()

print("Seuraavat elokuvat on julkaistu ennen vuotta 2000:")
for movie in old_movies:
    print(movie)