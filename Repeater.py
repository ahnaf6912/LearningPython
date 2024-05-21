def repeater(word):
    double = ""
    for character in word:
        double = double + str(character) + str(character)
    print(double)

a = input("what is your string ")
repeater(a)