def pythagorean_triplet(integer_1, integer_2, integer_3):
    if integer_1 > integer_2 and integer_1 > integer_3:
        a = integer_1
        b = integer_3
        c = integer_2
    elif integer_2 > integer_1 and integer_2 > integer_3:
        a = integer_2
        b = integer_1
        c = integer_3
    elif integer_3 > integer_1 and integer_3 > integer_2:
        a = integer_3
        b = integer_2
        c = integer_1
    if a ** 2 != c ** 2  + b ** 2:
        print(False)
    else:
        print(True)

a = int(input("What is your first number "))
b = int(input("What is your second number "))
c = int(input("What is your third number "))
pythagorean_triplet(a,b,c)
