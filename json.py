import json

json_string = '{"name": "Aditya", "age": 18, "city": "kolhapur"}'
data = json.loads(json_string)

print("Dictionary:")
print(data)

json_data = json.dumps(data, indent=4)

print("\nJSON String:")
print(json_data)

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nJSON data written to file")

with open("data.json", "r") as file:
    file_data = json.load(file)

print("\nJSON data read from file:")
print(file_data)
