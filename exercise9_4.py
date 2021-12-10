import functions

query = input("Syötä tapahtuman osallistujat pilkulla eroteltuna:\n")
# Matti Korhonen, Timo Virtanen, Tuula Salminen, Juha Mäkinen, Ritva Heikkilä

list_people = functions.show_numbered_list("Ilmoittautumisjärjestys", query)
print(list_people)


