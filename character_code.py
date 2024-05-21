def character_code(character):
    if character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9" or character == "0":
        print(ord(character))

    
    elif character == character.upper():
        print(ord(character))

        print(ord(character.lower()))
    elif character == character.lower():
        print(ord(character))
        print(ord(character.upper()))

a = input("What is your character ")
character_code(a)