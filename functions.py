def show_personal_info(name, location, occupation):
    response = print(f"{name}\n{location}\n{occupation}")
    return response


def count_seconds(hours, minutes, seconds):
    result = ((hours * 60) * 60) + (minutes * 60) + seconds
    return result


def magazine_serial_check(serial):
    # is the 4th character a hyphen:
    if serial[4] == '-':
        # remove the hyphen
        serial = serial.replace('-', '')

        # is the length now 8 characters:
        if len(serial) == 8:

            # is it all numbers:
            if serial.isnumeric():

                # if all conditions are met, is_ISSN is assigned
                # the value True
                is_ISSN = True
                return is_ISSN

            # all other cases will return is_ISSN = False
            else:
                is_ISSN = False
                return is_ISSN
        else:
            is_ISSN = False
            return is_ISSN
    else:
        is_ISSN = False
        return is_ISSN


#def show_numbered_list(title, data):
    #list_people = data.split(",")
   # for person in list_people:


def box_volume(width, height, depth):
    boxvolume = width * height * depth
    boxvolume = round(boxvolume, 2)
    return boxvolume


def ball_volume(radius):
    # importing pi and pow from math
    from math import pi, pow

    ballvolume = (4 * pi * (pow(radius, 3)) / 3)
    ballvolume = round(ballvolume, 2)

    return ballvolume


def pipe_volume(radius, length):
    from math import pi, pow

    pipevolume = pi * (pow(radius, 2)) * length
    pipevolume = round(pipevolume, 2)

    return pipevolume

