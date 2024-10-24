def square_digit(number):
    add = ""
    for digits in number:
        squaring = int(digits) * int(digits)
        add = add + str(squaring)
    print(add)

a = input("number ")
square_digit(a)


