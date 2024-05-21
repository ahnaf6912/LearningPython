def largest_number(array):
    total = 0
    for number in array:
        if int(number) > total:
            total = int(number)
    print(total)

a = input("What is ur set of numbers ")
b = a.split(",")
largest_number(b)

        
