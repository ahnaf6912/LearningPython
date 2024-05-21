def counting_words(sentence):
    letter_flag = False
    space_flag = False
    word = 0
    for letter in sentence:
        if letter != " ":
            letter_flag = True
        if letter_flag == True:
            if letter == " ":
                space_flag = True
        if space_flag == True and letter_flag == True:
            word = word + 1
            space_flag = False
            letter_flag = False
    word = word + 1
    print(word)
       
  
            
a = input("What is your sentence? ")
counting_words(a)