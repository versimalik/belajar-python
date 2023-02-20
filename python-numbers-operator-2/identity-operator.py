# Identity Operator

number1 = 15 # integer object
number2 = 14 # integer object
number3 = 14 # integer object
text1 = "15" # string object

print(number1 is text1)
# returns False
# because they are different objects

print(number2 is number3)
# returns False
# because they are the same objects

print(number1 is not text1)
# returns True
# because they are different objects

print(number1 is not number2)
# returns True
# because they are different objects