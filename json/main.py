# JSON = Javascript Object Notation
import json

data_json = '{"firstName":"Jane","lastName":"Doe","hobbies":["running","sky diving","singing"],"age":35,"children":[{"firstName":"Alice","age":6},{"firstName":"Bob","age":8}]}'

converted_json = json.loads(data_json)
beautify_json = json.dumps(converted_json, indent=3)
print(beautify_json)