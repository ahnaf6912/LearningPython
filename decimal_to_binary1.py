from reverse import reverse
def decimal_to_binary1(decimal):
    remainders = ""

    while decimal >= 2:
        remainder = int(decimal % 2)
        print(remainder)
        decimal = int(decimal / 2)
        remainders = remainders + str(remainder)


    remainders = remainders + str(decimal)
    print(remainders)

    b = reverse(remainders)
    print(b)

a = int(input("number "))
decimal_to_binary1(a)