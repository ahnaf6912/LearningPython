def greetings(list):
    greet = []
    greeting = "hello "
    gree = " "
    for names in list:
        greet.append(greeting + names)
    print(greet)
    for items in greet:
        gree = items + ", " + gree
    print(gree)
a = input("name ")
b = a.split(",")
greetings(b)