def replace_character(text, replace):
    str = ""
    for characters in text:
        if characters == replace:
            str = str + "*" 
        else:
            str = str + characters
    print(str)    

a = input("What is ur text ")
b = input("What do you want to replace ")
replace_character(a,b)

