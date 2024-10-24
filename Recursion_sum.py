def recursion_sum(number):
    total = 1
    for numbers in range (1, int(number)):
        total = total + (numbers + 1)
    print(total)

a = input("What is your number ")
recursion_sum(a)