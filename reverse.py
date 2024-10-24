def reverse(number):
    add = ""
    index = len(number)
    for digit in number:
        reverse = number[index - 1]
        add = add + reverse
        index = index - 1
    return add 


