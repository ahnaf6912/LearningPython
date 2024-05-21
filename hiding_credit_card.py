def hiding_card(credit_card):
    text = ""
    for number in range(0, len(credit_card)):
        if number < len(credit_card) - 4:
            text = text + '*'
        else:
            text =  text + credit_card[number]
    print(text)



a = input("What is your credit card number ")
hiding_card(a)