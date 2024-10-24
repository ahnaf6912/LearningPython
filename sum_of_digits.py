def sum_of_digits(number):
    sum = 0
    for digits in number:
        sum = sum + int(digits)
    print(sum)

a = input("What is your number ")
sum_of_digits(a)