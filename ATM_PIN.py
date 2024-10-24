def ATM_PIN(code):
    flag = False
    for characters in code:
        if characters == "1" or characters == "2" or characters == "3" or characters == "4" or characters == "5" or characters == "6" or characters == "7" or characters == "8" or characters == "9" or characters == "0":
         flag = True
        else:
         flag = False
    if flag == True:
       if len(code) == 4 or len(code) == 6:
          flag = True
       else:
             flag = False
    print(flag)
          

a = input("what is your pin code? ")
ATM_PIN(a)
