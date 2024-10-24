def compound_interest(p,t,r,n):
    for compounds in range(0, n*t):
        p = (r * p) + p
    print(p)

p = float(input("what is your principal "))
t = int(input("time in years "))
r = float(input("rate "))
n = int(input("compunding periods per year "))
compound_interest(p,t,r,n)

    

