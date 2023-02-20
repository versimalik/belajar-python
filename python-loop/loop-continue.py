# loop - continue
# in while loop

number = 0

# for example
# we only want to skip number 3
# so we can use if-condition

while number <= 10:
	number += 1
	if number == 3:
		continue
	print(number)

# when number is 3
# it will be skipped

# in for loop

for i in range(1,10):
	if i == 3:
		continue
	print(i)

# when 'i' is 3
# it will be skipped