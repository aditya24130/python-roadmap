import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

data = response.json()

print("नाव :", data["name"])
print("ईमेल :", data["email"])
print("शहर :", data["address"]["city"])
print("यूजरनेम  :", data["username"])