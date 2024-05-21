def max_edge_triangle(sides):
    max_edge = (int(sides[0]) + int(sides[1])) - 1
    print(max_edge)

a = input("input 2 sides of triangle ")
b = a.split(",")
max_edge_triangle(b)