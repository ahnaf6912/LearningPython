number_of_inputs = int(input("how many inputs? "))
sentence = ""
array_string = []
array_number = []
total_add = 0
print(number_of_inputs)
# takes amount of input required and seperating them into an array of strings and numbers
for inputs in range (0, number_of_inputs):
    inputs = input("random input ")
    if inputs.isnumeric() == True:
        array_number.append(inputs)
    else:
        array_string.append(inputs)
print(array_string)
# Takes the array of strings and uses it to form a sentence
for words in array_string:
    sentence = sentence + " " + words
print(sentence.strip())
# Takes the even numbers in the array and adds them
for numbers in array_number:
    if int(numbers) % 2 == 0:
        total_add = total_add + int(numbers)
print(total_add)
# display the strings which are in even position in the array
for index in range(0, len(array_string)):
    if index % 2 == 0:
        print(array_string[index])




















# # print first item
# print(array_input[0])
# # print last item
# print(array_input[len(array_input) - 1])
# # if the array contains atleast 3 items, print the 3rd item
# if len(array_input) >= 3:
#     print(array_input[2])


    