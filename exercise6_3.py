# importataan tämä mediaania ja moodia varten
import statistics

# montako opiskelijaa ryhmässä on
num1 = int(input("Opiskelijoiden lukumäärä:\n"))

# luodaan lista arvosanoille
gradestotal = []

# kysytään arvosanat silmukalla ja lisätään listaan
for x in range(num1):
    grades = float(input("Anna opiskelijan arvosana:\n"))
    gradestotal.append(grades)

# lasketaan keskiarvo ja tulostetaan se
mean = (sum(gradestotal)) / num1

# tein huvikseni tuplen josta sanallinen arvio haetaan :)
words = (
    "Huono tulos",
    "Heikko tulos",
    "Tyydyttävä tulos",
    "Hyvä tulos",
    "Kiitettävä tulos"
)

# tarkistetaan mikä sanallinen arvio tulostetaan
print(f"Keskiarvo: {mean}")
if 0 < mean <= 1:
    print(words[0])
elif 1 <= mean < 2:
    print(words[1])
elif 2 <= mean < 3:
    print(words[2])
elif 3 <= mean < 4:
    print(words[3])
elif 4 <= mean <= 5:
    print(words[4])

# lasketaan mediaani ja tyyppiarvo
mediangrade = statistics.median(gradestotal)
print(f"Arvosanojen mediaani: {mediangrade}")
gradesmode = statistics.mode(gradestotal)
print(f"Yleisin arvosana: {gradesmode}")
