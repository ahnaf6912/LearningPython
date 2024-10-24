def binary_to_decimal(binary):
    decimal = 0
    multiple = len(binary)
    for digits in binary:
        multiple = multiple - 1
        decimal_numbers = int(digits) * (2 ** multiple)
        decimal = decimal + decimal_numbers 
    print(decimal)


a = input("Input binary number: ")
binary_to_decimal(a)