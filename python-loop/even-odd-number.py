range_input = int(input("How many loops? "))
menu = input("Display even or odd numbers? (even/odd) ")

if menu == "even":
	for i in range(range_input+1):
		if i % 2 == 0:
			print(i)
elif menu == "odd":
	for i in range(range_input+1):
		if i % 2 == 1:
			print(i)