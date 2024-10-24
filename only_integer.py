def only_integer(elements):
    integer = []
    for item in elements:
        for character in item:
            if character != '0' and character != '1' and character != '2' and character != '3' and character != '4' and character != '5' and character != '6' and character != '7' and character != '8' and character != '9':
                break
        else: integer.append(item)
    print(integer)


a = input("item ")
b = a.split(",")
only_integer(b)