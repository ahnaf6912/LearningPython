def paper_fold(fold):
    thickness = 0.5
    for folds in range(0, int(fold)):
        thickness = thickness * 2
    print(thickness)

a = input("how many times do you want to fold? ")
paper_fold(a)

