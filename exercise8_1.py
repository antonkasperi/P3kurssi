# importing required modules
from colorama import Fore, Style
from datetime import datetime

# creating a list for the ages, turning the requested values into integers which are then inserted into the list
ages = []
for x in range(0, 5):
    age = int(input(f"Anna henkilön {x+1} syntymävuosi:\n"))
    ages.append(age)

# current year into a variable
yearnow = datetime.now().year

# calculating the ages in a loop and save them into another list
checktheages = []
for age in ages:
    age = yearnow - age
    checktheages.append(age)

# check if the ages are ok or not, print results
for age in checktheages:
    if 0 <= age <= 125:
        print(Fore.GREEN + f"{age} vuotta, ikä OK!")
    elif age < 0 or age > 125:
        print(Fore.RED + f"{age} vuotta, ikä ei oikeassa muodossa.")
print(Style.RESET_ALL + "Valmis!")
