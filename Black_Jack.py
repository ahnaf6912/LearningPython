def black_jack(cards):
    sequence = []
    total = 0
    for card in cards:
        if card == "2" or card == "3" or card == "4" or card == "5" or card == "6":
            card = 1
        elif card == "7" or card == "8" or card == "9":
            card = 0
        elif card == "10" or card == "J" or card == "Q" or card == "K" or card == "A":
            card = -1
        sequence.append(card)
    print(sequence)
    for numbers in sequence:
            total = total + int(numbers)
    print(total)

a = input("what is your sequence of cards seperated by comma ")
b = a.split(",")
black_jack(b)

