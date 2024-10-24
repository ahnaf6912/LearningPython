def edabit(range1, range2):
    for digits in range(int(range1), int(range2) + 1):
        if digits % 5 == 0 and digits % 3 == 0:
            digits = "EdaBit"
        elif digits % 3 == 0:
            digits = "Eda"
        elif digits % 5 == 0:
            digits = "Bit"
        print(digits)

a = input("what is the beginning for your range ")
b = input("what is the last number in your range ")
edabit(a, b)