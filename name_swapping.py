def name_swapping(name):
    swap_name = name[0]
    name[0] = name[1]
    name[1] = swap_name
    print(name[0] + " " + name[1])

a = input("What is ur full name ")
b = a.split(" ")
name_swapping(b)
