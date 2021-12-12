# kysytään käyttäjältä mitä hän haluaa tehdä
query = input("Haluatko lukea vai kirjoittaa vieraiskirjaan? (l/k)\n")

# jos vastaus on "k"
if query == "k":
    # avataan tiedoston append-muodossa
    guestbook_handle = open("guestbook.txt", "a")

    # pyydetään viesti
    prompt = input("Kirjoita uusi viesti:\n")
    # lisätään viesti omalle rivilleen
    guestbook_handle.write(f"\n{prompt}")

    # suljetaan yhteys
    guestbook_handle.close()

# jos käyttäjä haluaa lukea viestejä:
elif query == "l":
    # avataan read-muodossa
    guestbook_handle = open("guestbook.txt", "r")
    # tehdään muuttujasta lista ja tulostetaan silmukassa
    contents = guestbook_handle.read()
    lines = contents.split("\n")
    for line in lines:
        print(line)

    # ja lopuksi tiedosto sulki
    guestbook_handle.close()
