import json

# .load() method used to convert in-file JSON
with open("json_file.json","r") as file:
	python_dict = json.load(file)

# JSON is now Python object
# print(python_dict)
print(python_dict['country'])
print(python_dict['email'])
