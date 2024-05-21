def counting_vowels(sentence):
    sum = 0
    for characters in sentence:
        if characters.upper() == "A" or characters.upper() == "E" or characters.upper() == "I" or characters.upper() == "O" or characters.upper() == "U":
            sum = sum + 1
    
    print(sum)

a = input("write a sentence ")
counting_vowels(a)
