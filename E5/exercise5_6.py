# luodaan dict
movie = {
    "name": "Pulp Fiction",
    "year": 1994,
    "director": "Quentin Tarantino",
    "genre": "Rikos, Draama",
    "duration": 154
}

# tulostus silmukalla
print("Silmukalla:\n")
for details in movie:
    print(movie[details])
print()

# tulostus ilman silmukkaa
print("Ilman silmukkaa:\n")
print(movie["name"])
print(movie["year"])
print(movie["director"])
print(movie["genre"])
print(movie["duration"])