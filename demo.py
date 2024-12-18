import requests

url="https://catfact.ninja/fact"

response=requests.get(url)
response.text
response.status_code

print(response)