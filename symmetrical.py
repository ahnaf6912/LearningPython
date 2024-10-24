def symmetrical(number):
    list = ""
    index = len(number)
    for characters in number:
        reverse = number[index - 1]
        list = list + reverse
        index = index - 1
    if list == number:
        print(True)
    else:
        print(False)



a = input("what is your number ")
symmetrical(a)