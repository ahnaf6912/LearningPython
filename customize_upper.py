def customize_upper(word):
    text = ""
    for index in range(0, len(word)):
        if (index + 1) % 3 == 0:
           text = text + word[index].upper()
        else:
            text = text + word[index]
    print(text)

a = input("What is ur word ")
customize_upper(a)