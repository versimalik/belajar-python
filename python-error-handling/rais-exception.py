print("I like python app")
print("=================")

loop = int(input("Enter a number: "))

if loop <= 1:
	raise Exception("Number must be > 1")
	print("sadasdas")
else:
	for i in range(loop):
		print("I Like python!")