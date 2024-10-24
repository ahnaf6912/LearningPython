def probability_1(array, n):
    favourable = 0
    for numbers in array:
        if int(numbers) >= n:
            favourable = favourable + 1
    probability = 100 * (favourable / len(array))
    print(probability)

a = input("input an array ")
b = int(input("what is the number you want to find the probability of? "))
c = a.split(",")
probability_1(c, b)
