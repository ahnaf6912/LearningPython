def missing_number(sequence):
    list = []
    for number in range(1, 10):
        if str(number) not in sequence:
            print(number)

a = input("What is your sequnce (range 1 to 10 in any order) ")
b = a.split(",")
missing_number(b)
