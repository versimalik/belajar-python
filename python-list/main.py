numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fruits = ["apple", "banana", "cherry"]
cars = ["toyota", "volvo", "honda", "suzuki"]
names = ["Andi", "Adit", "Cyntia", "Debby", "Andi"]

# acessing item
print(numbers[2])
print(fruits[1])
print(cars[3])
print(f"{names[2]} and {names[3]} are girls")

# add new item using .append()
fruits.append("durian")
print(fruits)

# add new item using .insert()
fruits.insert(2, "jackfruit")
print(fruits)

# modify item
names[4] = "Andi Toni"
names[0] = "Andi Heri"
print(names)

# remove item using .remove()
cars.remove("volvo")
print(cars)

# remove item using .pop()
fruits.pop(3)
print(fruits)

# clear items in list using .clear()
names.clear()
print(names)

# check if there is any jackfruit inside fruits list
if "jackfruit" in fruits:
	print("Yes, there is jackfruit in fruits list!")

if "cherry" not in fruits:
	fruits.append("cherry")

print(fruits)