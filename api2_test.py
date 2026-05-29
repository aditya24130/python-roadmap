import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")

response = requests.get(api_url)

data = response.json()
print("API KEY :", api_key)
print("नाव :", data["name"])
print("ईमेल :", data["email"])