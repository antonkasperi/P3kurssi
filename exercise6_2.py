# boolean joka kontrolloi while-silmukkaa
running = True

while running:
    choice = int(input("Minkä luvun kertotaulun haluat nähdä? (1-10). 0 lopettaa ohjelman.\n"))
    # jos luku on alle 0 tai yli 10, hypätään yli ja kysytään uudestaan
    if choice > 10 or choice < 0:
        print("Vääränlainen luku.")
        continue
    # jos luku on 0, lopetetaan ohjelma
    elif choice == 0:
        running = False
        exit()
    else:
        # toinen silmukka, joka tulostaa kertotaulun
        for i in range(1, 11):
            print(f"{choice} x {i} = {choice * i}")
        print()
