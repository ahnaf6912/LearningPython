number_of_inputs = int(input("how many inputs? "))
array_input = []
print(number_of_inputs)
for inputs in range (0, number_of_inputs):
    inputs = input("random input ")
    array_input.append(inputs)
if len(array_input) % 2 == 0:
    print(array_input[(len(array_input) // 2) - 1])
else:
    print(array_input[len(array_input) // 2])




















# # print first item
# print(array_input[0])
# # print last item
# print(array_input[len(array_input) - 1])
# # if the array contains atleast 3 items, print the 3rd item
# if len(array_input) >= 3:
#     print(array_input[2])


    