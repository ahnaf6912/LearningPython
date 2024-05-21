def christmas(date):
    if date[1] == "12" and date[2] == "24":
        print(True)
    else:
        print(False)

a = input("write a date seperated by comma ")
b = a.split(",")
christmas(b)