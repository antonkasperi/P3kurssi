import functions

# requesting the people attending
query = input("Syötä tapahtuman osallistujat pilkulla eroteltuna:\n")
# Matti Korhonen, Timo Virtanen, Tuula Salminen, Juha Mäkinen, Ritva Heikkilä

# splitting the data into a list
list_people = query.split(",")
# removing spaces
list_people = [p.strip() for p in list_people]

# call 1 with the appropriate title
title = "Ilmoittautumisjärjestys:"
functions.show_numbered_list(title, list_people)
print()

# call 2
title = "Aakkosjärjestys etunimen perusteella:"
# sorting the created list according to the first letter of the first name
list_people = sorted(list_people, key=str)
functions.show_numbered_list(title, list_people)
print()

# call 3
title = "Aakkosjärjestys sukunimen perusteella:"
# flipping the names and sorting the new list
list_people = [" ".join(reversed(p.split(" "))) for p in list_people]
list_people = sorted(list_people, key=str)
functions.show_numbered_list(title, list_people)
