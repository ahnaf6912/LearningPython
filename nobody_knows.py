def nobody_knows(string):
    o_count = 0
    x_count = 0
    for letter in string:
        if letter.upper() == "O":
            o_count = o_count + 1
        if letter.upper() == "X":
            x_count = x_count + 1
    if x_count == o_count:
        print(True)
    else:
        print(False)
    # if string.count("o") == string.count("x"):
    #     print(True)
    # else:
    #     print(False)

a = input("What is ur string ")
nobody_knows(a)