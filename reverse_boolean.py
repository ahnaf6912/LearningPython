def reverse_boolean(input):
    if input.upper() == "TRUE":
        print(False)
    elif input.upper() == "FALSE":
        print(True)
    else:
        print("boolean expected")

a = input("input ")
reverse_boolean(a)