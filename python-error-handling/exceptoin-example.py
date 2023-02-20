print("Simple Divider")
print("============")

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

try:
	result = int(number1)/int(number2)
	print(f"{number1} / {number2} = {result}")
except ZeroDivisionError:
	print("Number(s) cannot be 0")
except ValueError:
	print("You should input number(int) value")
finally:
	print("Simple Divider Termninated!")