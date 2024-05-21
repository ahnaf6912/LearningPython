def adding_digits(number):
    negative = False
    total = 0
    for num in number:
        if num == "-":
            negative = True
        if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6" or num == "7" or num == "8" or num == "9" or num == "0":
            if negative == True:
                total = int(num) * -1 + total
                negative = False
            else:
                total = int(num) + total
    print(total)
           

a = input("What is ur number: ")
adding_digits(a)
