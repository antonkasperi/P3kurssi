from colorama import Back
from random import randrange

secretnumber = randrange(1, 20)
query = int(input("Arvaa numero (1-20:\n"))

wrong = True
try:
    while wrong:
        if query < secretnumber:
            query = int(input(Back.BLUE + "Liian matala\n"))
            continue
        elif query > secretnumber:
            query = int(input(Back.RED + "Liian korkea\n"))
            continue
        else:
            print(Back.GREEN + "ONNEKSI OLKOON!")
            wrong = False
except ValueError:
    print(Back.RESET + "Annoit tekstiä! Aloita alusta.")

