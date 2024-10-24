def showdown(p1,p2):
    gun_1 = p1.index("Bang!")
    gun_2 = p1.index("Bang!")
    print(gun_1)
    print(gun_2)
    if gun_1 > gun_2:
        print("p1")
    elif gun_1 < gun_2:
        print("p2")
    elif gun_1 == gun_2:
        print("tie, you both die")

a = input("p1 shot ")
b = a.split(" ")
c = input("p2 shot ")
d = c.split(" ")
showdown(b,d)