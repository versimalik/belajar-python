# dicionary => key : value
# object

student = {"name": "Jaka", "address": "Jakarta Barat"}


}

# display dict keys
print(car.keys())

# access item
print(car["brand"])

# add new item
car["owner"] = "Jaka"
print(car)

# modify item
car["color"][0] = "white"
print(car)

# modify item
car["color"] = ["red", "black"]
print(car)

# remove item
car.pop("color")
print(car)

# remove the last item
car.popitem()
print(car)
