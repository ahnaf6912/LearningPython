def odd_integer(array):
    dictionary = {}
    for number in array:
        if array.count(number) % 2 != 0:
            dictionary[number] = array.count(number)
    print(dictionary)

a = input("input a list of numbers seperated by comma ")
b = a.split(",")
odd_integer(b)