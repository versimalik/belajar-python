print("Bitwise Shift Calculator")
print("========================")

decimal_number = int(input("Enter a decimal number: "))
shift = input("Right or Left? ").lower()
number_of_shift = int(input("Number of shift: "))

if shift == "right":
	result = decimal_number >> number_of_shift
	print(f"{decimal_number} >> {number_of_shift} = {result}")
elif shift == "left":
	result = decimal_number << number_of_shift
	print(f"{decimal_number} << {number_of_shift} = {result}")
else:
	print("You have input a wrong format!")