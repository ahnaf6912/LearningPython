def upper_index(text):
    list = []
    for index in range(0, len(text)):
        if text[index] == text[index].upper():
            list.append(index)
    print(list)

a = input("What is your text ")
upper_index(a)
            
