def add_index(array):
    list = []
    for index in range(0, len(array)):
        increase = int(index) + int(array[index]) 
        list.append(increase)
    print(list)
a = input("enter a set of numbers ")
b = a.split(",")
add_index(b)
        

