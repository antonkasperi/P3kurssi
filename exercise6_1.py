# alustetaan muuttujat; biggest on vinkin apumuuttuja ja choice
# käyttäjän antamille numeroille
biggest = 0
choice = 0

# for-silmukka, joka pyytää viisi kokonaislukua. tässä tapauksessa ei tarvitse
# erillisiä muuttujia joka numerolle, koska vain suurin pyydetään lopuksi
for x in range(5):
    choice = int(input("Anna numero:\n"))
    # jos numero ei ole positiivinen kokonaisluku, ohjelma ilmoittaa siitä
    # ja sen jälkeen aloittaa silmukan alusta huomioimatta virheellistä syötettä
    if choice <= 0:
        print("Anna positiivinen kokonaisluku!")
        continue

    # jos käyttäjän antama luku on isompi kuin sen hetkinen suuri luku, tallennetaan
    # tämä muuttujaan 'biggest'
    elif choice > biggest:
        biggest = choice
    # jos luku on pienempi, ohitetaan ja aloitetaan alusta
    else:
        pass
print()

# tulostetaan isoin syötetty luku.
print(f"Suurin käyttäjän luku: {biggest}")
