# list item is stored in square bracket
# duplicate item allowed

numbers = [2, 3, 5, 6, 7, 8, 3, 4, 56]
fruits = ["apple","banana","cherry"]
cars = ["toyota","volvo","honda",]
names = ["Andi","Abby","Andi","Benny"]

order_number = 0

print(type(numbers)) # data type
print(len(numbers)) # length
print(numbers)

# accessing list item
print(cars[1])
print(names[3])
print(f"{names[1]} dan {names[3]}")

# add list item
fruits.append("mango")
print(fruits)

cars.insert(1,"suzuki")
print(cars)


# remove list item
fruits.remove("apple")
print(fruits)

fruits.pop(2)
print(fruits)


# update list item
names[3] = "Benny Ahmad"
print(names)


for car in cars:
	print(f"{order_number}: {car}")
	order_number += 1