from math import pi
def weight(r,h):
    acir = r ** 2 * pi
    acyl = acir * h
    weight = acyl * .001
    print(str(round(weight, 2)) + " KG")

a = float(input("What is the radius of the cylinder "))
b = float(input("What is the height of the cylinder "))
weight(a,b)