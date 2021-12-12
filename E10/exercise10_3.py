import random

# creating a list
words_handle = open("wisewords.txt", "r")
words_content = words_handle.read()
words_list = words_content.split("\n")

# determining the list length
list_length = len(words_list) - 1

# creating a random index number
rand_index = random.randint(0, list_length)

# picking the daily aphorism based on the variable rand_index
thought_for_the_day = words_list[rand_index]

# printing
print("Päivän mietelause:")
print(thought_for_the_day)

words_handle.close()
