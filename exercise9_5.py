import functions

# boolean to control the while loop
running = True
while running:

    query = int(input("Valitse toimenpide (1-3), 0 lopettaa ohjelman:\n"))

    # input 0 ends the loop
    if query == 0:
        running = False

    # box volume
    elif query == 1:
        width = float(input("Anna laatikon leveys:\n"))
        height = float(input("Anna laatikon korkeus:\n"))
        depth = float(input("Anna laatikon syvyys:\n"))

        boxvolume = functions.box_volume(width, height, depth)
        print(f"Laatikon tilavuus: {boxvolume} m3")

    # circle volume
    elif query == 2:
        radius = float(input("Anna pallon säde:\n"))

        ballvolume = functions.ball_volume(radius)
        print(f"Pallon tilavuus: {ballvolume} m3.")

    # pipe volume:
    elif query == 3:
        radius = float(input("Anna putken säde:\n"))
        length = float(input("Anna putken pituus:\n"))

        pipevolume = functions.pipe_volume(radius, length)
        print(f"Putken tilavuus: {pipevolume} m3.")
