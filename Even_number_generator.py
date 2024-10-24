def even_number_generator(number):
    list = []
    for numbers in range(1, int(number) + 1):
        if numbers % 2 == 0:
            list.append(numbers)
    print(list)

a = input("input number ")
even_number_generator(a)
