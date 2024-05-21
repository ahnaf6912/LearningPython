def string_only(array):
    new_array = []
    for word in array:
        flag = True
        for character in word:
            if character != "1" and character != "2" and character != "3" and character != "4" and character != "5" and character != "6" and character != "6" and character != "7" and character != "8" and character != "9" and character != "0":
              flag = False
        if flag == True:
          new_array.append(word)
    print(new_array)

a = input("input an array ")
b = a.split(",")
string_only(b)
          
