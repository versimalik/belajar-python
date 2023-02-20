import json

data = {
	"employees":[
		{
			"firstName":"John",
			"lastName":"Doe"},
		{
			"firstName":"Anna",
			"lastName":"Smith"
		},
		{
			"firstName":"Peter",
			"lastName":"Jones"
		}
	]
}

print(type(data)) # data is a dictionary

# .dump() method used to convert python object
# into json text files
with open("data_file.json","w") as file:
	json.dump(data, file, indent=4)

# .dumps() method used to convert a json object
# to python object, to continue using it
print(json.dumps(data, indent=4))	