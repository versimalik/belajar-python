cars = ("toyota", "volvo", "honda", "suzuki")

print(type(cars))
print(cars)

# access item
print(cars[2])

# modify item
# cars[0] = "wuling" # it returns error
cars_list = list(cars)
cars_list[0] = "wuling"
cars = tuple(cars_list)
print(cars)

# remove item
cars_list = list(cars)
cars_list.pop(2)
cars = tuple(cars_list)
print(cars)

# clear items
cars.clear()
print(cars)