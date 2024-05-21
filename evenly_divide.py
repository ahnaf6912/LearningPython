def evenly_divide(starting, ending, divide):
    sum = 0
    for numbers in range(starting, ending + 1):
        if numbers % divide == 0:
            sum = sum + numbers
    print(sum)

a = int(input("What is the starting number? "))
b = int(input("What is the end range? "))
c = int(input("What is the divide? "))
evenly_divide(a,b,c)
            