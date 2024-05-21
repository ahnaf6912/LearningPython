def the_reverser(word):
    worde = ""
    for index in range(0, len(word)):
        last_index = (len(word) - 1) - index
        if word[index] == word[index].upper():
            worde = worde + word[last_index].lower()
        else:
            worde = worde + word[last_index].upper()
    print(worde)


    
    

a = input("What is the word ")
the_reverser(a)
