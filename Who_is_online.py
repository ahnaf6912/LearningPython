def who_is_online(online_list):
    for members in online_list:
        if len(online_list) == 0:
            print("no one is online")
        elif len(online_list) == 1:
             print(online_list[0] + " online")
        elif len(online_list) == 2:
             print(online_list[0] + " and " + online_list[1] + " are online")
        elif len(online_list) > 2:
             print(online_list[0] + " and " + online_list[1] + " and " + len(online_list) - 2 + " more online")
    
a = input("members online ")
b = a.split(",")
who_is_online(b)