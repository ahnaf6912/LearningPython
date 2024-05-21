def default_mood(mood):
    if mood != "":
        print("Today, I am feeling %s" % (mood))
    else:
        print("Today, I am feeling neutral")

a = input("How do you feel ")
default_mood(a)