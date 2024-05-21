def even_odd_digits(numbers):
    total_even = 0
    total_odd = 0
    negative = False
    for number in numbers:
        if number == "-":
            negative = True
        elif int(number) % 2 == 0:
            if negative == True:
                total_even = int(number) * -1 + total_even
                negative = False
            else:
                total_even = int(number) + total_even
        elif int(number) % 2 != 0:
            if negative == True:
                total_odd = int(number) + total_odd
                negative = False
            else:
                total_odd = int(number) + total_odd
    if total_even > total_odd:
        print(True)
    else:
        print(False)

a = input("What is your number ")
even_odd_digits(a) 

