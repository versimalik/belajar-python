# loop - break
# in while loop

number = 1

# for example
# we only want to print
# the first three numbers
# so we can use if-condition to break

while number <= 10:
	print(number)
	if number == 3:
		break
	number += 1

# loop will be terminated
# when number is 3

# in for loop

for i in range(1,10):
	print(i)
	if i == 3:
		break

# loop will be terminated
# when number is 3