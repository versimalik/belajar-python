# decimal to binary conversion

decimal_number = int(input("Enter a decimal number: "))

binary_number = bin(decimal_number).replace("0b","")

print(f"Binary of {decimal_number} is {binary_number}")