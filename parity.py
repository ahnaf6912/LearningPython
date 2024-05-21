def parity(number):
    sum = 0
    for num in number:
        sum = sum + int(num)
    if number % 2 == 0 and sum % 2 == 0:
        print(True)
    else:
        print(False)

a = input("Type your number: ")
parity(a)