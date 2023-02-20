import json

# store JSON text in a variable
json_string = """
	{
		"firstname": "Fanny",
		"lastname": "Lorenz",
		"city": "Shigatse",
		"country": "Senegal",
		"countryCode": "NO",
		"email": "Fanny.Lorenz@gmail.com"
	}
"""

# .loads() method used to convert in-file JSON
python_dict = json.loads(json_string)

# JSON is not Python object
print(type(python_dict))
print(python_dict['firstname'])
print(python_dict['lastname'])


