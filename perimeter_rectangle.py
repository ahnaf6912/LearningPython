def perimeter_rectangle(measurements):
    total_length = int(measurements[0]) * 2
    total_width = int(measurements[1]) * 2
    perimeter = total_length + total_width
    print(perimeter)

a = input("input length and width or rectangle ")
b = a.split(",")
perimeter_rectangle(b)