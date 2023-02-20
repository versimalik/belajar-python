import json

json_string = """
	{
		"firstname": "Fanny",
		"lastname": "Lorenz",
		"city": "Shigatse",
		"country": "Senegal",
		"countryCode": "NO",
		"email uses current data": "Fanny.Lorenz@gmail.com",
		"email from expression": "Fanny.Lorenz@yopmail.com"
	}
"""

print(json.loads(json_string))