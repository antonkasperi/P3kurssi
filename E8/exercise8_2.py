# import modules
from colorama import Back
from random import randrange

# set the random number into a variable
secretnumber = randrange(1, 20)
query = int(input("Arvaa numero (1-20:\n"))

# while the guess is wrong, the while loop will run and request new numbers
wrong = True
while wrong:
    if query < secretnumber:
        query = int(input(Back.BLUE + "Liian matala\n"))
        continue
    elif query > secretnumber:
        query = int(input(Back.RED + "Liian korkea\n"))
        continue
    # when the user guesses right, the boolean cuts the while loop and print out the message
    else:
        print(Back.GREEN + "ONNEKSI OLKOON!")
        wrong = False
