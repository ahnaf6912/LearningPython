from exist import exist
def set(list):
    set_list = []
    for item in list:
        if not exist(set_list, item):
           set_list.append(item)
    print(set_list)



a = input("input ur list ")
b = a.split(",")
set(b)