# Membership Operators

letter1 = "a"
number1 = 10

words = "Hello, world!"
numbers = [1, 2, 3, 4, 5] # list data type

print(letter1 in words)
# returns False, because
# there is no letter "a" in "Hello, world!"

print(number1 not in numbers)
# returns True, because
# there is no number 10 in numbers list

# membership operators can be used
# with only iterable object
# like, string, list, tuple, etc