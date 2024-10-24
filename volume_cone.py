from math import pi
def volume_cone(height, radius):
    volume = ((radius ** 2) * pi * height) / 3
    print(round(volume, 2))

height = int(input("What is the height of the cone "))
radius = int(input("What is the radius of the base "))
volume_cone(height, radius)