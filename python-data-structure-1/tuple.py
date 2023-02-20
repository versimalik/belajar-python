# tuple item is stored in round bracket
numbers = (0,1,2,3,4,5,6,7,8,9)
fruits = ("apple","banana","cherry")
cars = ("toyota","volvo","honda",)
names = ("Andi","Abby","Andi","Benny")

print(type(numbers))
print(len(numbers))

print(type(fruits))
print(len(fruits))

print(type(cars))
print(len(cars))

print(type(names))
print(len(names))

# accessing item by calling item index
# index is started from 0, NOT from 1

print(numbers[5])
# output: 5

print(fruits[2])
# output: cherry

print(cars[1])
# output: volvo

print(f"{names[3]} and {names[0]}")
# output: Benny and Andi