# listat
fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

inventory = [fruits, berries, vegetables]

# ja silmukat
for items in inventory:
    for food in items:
        print(food)
