import functions

# requesting the ISSN
query = input("Anna ISSN-sarjanumero:\n")

# creating the variable is_ISSN which will be
# assigned a boolean value in the function
is_ISSN = functions.magazine_serial_check(query)

# based on what the function return, the if clause is completed
if is_ISSN:
    print("Oikea ISSN.")
else:
    print("Väärä ISSN.")
