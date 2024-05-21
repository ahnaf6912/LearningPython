def finding_numbers(strings):
    sum = 0
    disctionary = {}
    for characters in strings:
        if characters == "1" or characters == "2" or characters == "3" or characters == "4" or characters == "5" or characters == "6" or characters == "7" or characters == "8" or characters == "9" or characters == "0":
            sum = int(characters) + sum
            disctionary[characters] = strings.count(characters)
    print(sum)
    print(disctionary)

        

a = input("input a set of characters ")
finding_numbers(a)
