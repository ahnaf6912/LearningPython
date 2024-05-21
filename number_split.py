def number_split(number):
    a = int(number / 2)
    b = 0
    if number % 2 != 0: 
        b = 1 + a
        if b < 0:
            b = -1 + a
    else:
        b = a
    print(int(a), int(b))

a = int(input("What is your number? "))
number_split(a)

