print("Input your grade: A/B/C")
grade = input().upper()

# checking 'grade'
# if 'A', print 'congratulations'
# if 'B', print 'good job'
# if 'C', print 'good luck next time'
# if none of them, print 'wrong input'

if grade == "A":
	print("Congratulation!")
elif grade == "B":
	print("Good Job!")
elif grade == "C":
	print("Good luck next time!")
else:
	print("Wrong input!")

# 'else' statement added
# to create another action
# if none of conditions abouve fulfilled