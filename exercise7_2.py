# listat
fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

inventory = [fruits, berries, vegetables]

# ja silmukat
for items in inventory:
    for froot in fruits:
        print(froot)
    for berry in berries:
        print(berry)
    for vegetal in vegetables:
        print(vegetal)
    break

# silmukka lopettaa yhden iteraation jälkeen