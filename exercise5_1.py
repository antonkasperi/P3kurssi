# while ja for loopit
counter = 1
while counter <= 50:
    print(counter)
    counter = counter + 1

for x in range(50):
    print(x+1)

# numeroiden 1-30 summa
sum = 0
for y in range(1, 31):
    sum = sum + y

print(f"Summa: {sum}")

# vuosiluvut
text = ""
for year in range(2005, 2011):
    text = text + str(year) + " "

print(text)
