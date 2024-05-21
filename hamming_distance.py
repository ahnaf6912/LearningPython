def hamming_distance(real, fake):
    total = 0
    if real == fake:
        print(0)
    else:
        for index in range(0, len(real)):
            if real[index] != fake[index]:
                total = total + 1
        print(total)

a = input("input a text ")
b = input("input a fake text ")
hamming_distance(a, b)
