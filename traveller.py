def travelling(cities):
    i = 0
    sum = 1
    while i < int(cities):
        i = i + 1
        sum = sum * i
    print(sum)
        
        

a = input("what is the number of cities ")
travelling(a)