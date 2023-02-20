import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(api_url)
response_json = response.json()

# print(response_json)

for todo in response_json:
	if todo['userId'] == 10 and todo['completed'] == True:
		print(json.dumps(todo, indent=3))