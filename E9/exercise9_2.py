import functions

# requesting variable values
hours = int(input("Anna tunnit:\n"))
minutes = int(input("Anna minuutit:\n"))
seconds = int(input("Anna sekunnit:\n"))

# calling the correct function  and printing the result
seconds_total = functions.count_seconds(hours, minutes, seconds)
print(f"Yhteensä {seconds_total} sekuntia.")