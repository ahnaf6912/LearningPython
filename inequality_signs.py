def  inequality_signs(signs):
    flag = False
    if signs[1] == "<" and int(signs[0]) < int(signs[2]):
        flag = True
    if signs[1] == ">" and int(signs[0]) > int(signs[2]):
        flag = True
    if signs[3] == "<" and int(signs[2]) < int(signs[4]):
        flag = True
    if signs[3] == ">" and int(signs[2]) > signs[4]:
        flag = True
    print(flag)

a = input("input an inequality ")
inequality_signs(a)
    


