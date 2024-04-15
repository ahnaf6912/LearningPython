def consonant(sentence):
    c = {}
    for letter in sentence:
        if letter.upper() != "A" and letter.upper() != "E" and letter.upper() != "I" and letter.upper() != "O" and letter.upper() != "U" and letter !=' ':
            if c.get(letter) == None:
                c[letter] = 0
            c[letter] = c[letter] + 1
    print(c)
        
a = input("Type ur sentence ")
consonant(a)