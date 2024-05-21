def replace_vowels(sentence, symbol):
    for letter in sentence:
        if letter.upper() == "A" or letter.upper() == "E" or letter.upper() == "I" or letter.upper() == "O" or letter.upper() == "U":
            letter = symbol
    print(sentence)

a = input("type a word or sentence ")
b = input("type a symbol ")
replace_vowels(a,b)