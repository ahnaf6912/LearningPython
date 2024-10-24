from reverse import reverse
def palindrome(number1, number2):
    count = 0
    for digit in range(int(number1), int(number2) + 1):
        reversa = reverse(str(digit))
        if reversa == str(digit):
           count = count + 1
    print(count)
a = input("starting range ")
b = input("end range ")
palindrome(a, b)

