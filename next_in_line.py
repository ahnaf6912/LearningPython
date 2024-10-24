def next_in_line(sequence, next):
    sequence.pop(0)
    sequence.append(next)
    print(sequence)

a = input("enter sequence ")
b = a.split(",")
c = input("next in line ")
next_in_line(b,c)
    