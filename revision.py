def average_grade(a,b,c,d):
    total = a + b + c + d
    if total > 400 or a > 100 or b > 100 or c > 100 or d > 100:
        print("Check your grades again ")
    else:
        average = total / 4
        print(average)
    
a = int(input("What is your first grade: "))
b = int(input("What is your second grade: "))
c = int(input("What is your third grade: "))
d = int(input("What is your fourth grade: "))
average_grade(a,b,c,d)

