import requests
import os

access_key = os.environ.get("ACCESS_KEY")

url = f"http://api.exchangeratesapi.io/v1/latest?access_key={access_key}"

try:
    response = requests.get(url)
    base_data = response.json()
except requests.RequestException:
    raise Exception("Unable to retrieve information from ExchangeAPI")
