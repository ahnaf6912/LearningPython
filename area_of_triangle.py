def area_of_triangle(measurements):
    area = int(measurements[0]) * int(measurements[1]) / 2
    print(area)

a = input("input triangle measurements ")
b = a.split(",")
area_of_triangle(b)