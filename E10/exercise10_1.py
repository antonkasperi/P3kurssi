# handle
artists_handle = open('artists.txt', 'r')

# creating the list
content = artists_handle.read()
lines = content.split("\n")

# for-loop to print out the list
for line in lines:
    print(line)

# closing the file connection
artists_handle.close()