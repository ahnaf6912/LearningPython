def filter_string(array):
    list = []
    for items in array:
        if items.isnumeric() == True:
            list.append(items)
    print(list)

a = input("input a list ")
b = a.split(",")
filter_string(b)

