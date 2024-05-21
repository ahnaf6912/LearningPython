def power_calculator(electricity):
    power =  int(electricity[0]) * int(electricity[1])
    print(power)

a = input("input voltage and current ")
b = a.split(",")
power_calculator(b)