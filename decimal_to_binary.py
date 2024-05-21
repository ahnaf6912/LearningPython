def decimal_to_binary(number):
    remainder = 0
    result = 0
    remainders = []
    while (True):
        remainder = number % 2
        remainders.append(remainder)
        result = int(number / 2)
        number = result
        if result == 1:
            remainder = 1
            remainders.append(remainder)
            break
        
    print(remainders)
    binary = len(remainders - 1)
    remainders[0] = len(remainders - 1)
    binary = remainders[0]
    print(remainders)
    

a = int(input("What is your number? "))
decimal_to_binary(a)



        
        

