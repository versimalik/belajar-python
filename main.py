import pprint
# Dictionary is used to store data values in key:value pairs.
# and is stored in curly brackets

student = {"name" : "Jaka", "address" : "Jakarta"}

car = {
	"model" : "truck",
	"brand" : "ford",
	"electric" : False,
	"year" : 2010,
	"price" : 140000000,
	"color" : ["red", "black", "white"]
}

print(type(student))
print(student)

print(type(car))
print(car)

print(student.keys())
print(student["name"])

print(car.keys())
print(car["brand"])

car["color"] = "red"
car["price"] = 140000
print(car)

car["year"] = 2011
car.update({"color" : ["red","black"]})
print(car)

car.pop("model")

car.popitem()

name = dict(name = "Jamal", address = "Jakarta", age = 18)
print(type(name))

# it will create the same like
"""

student = {
	"name" : "Jamal",
    "address" : "Jakarta"
}

"""
