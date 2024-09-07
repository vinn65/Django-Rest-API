import requests

endpoint =  "http://127.0.0.1:8000/api/products/"

get_response = requests.get(endpoint)

print(get_response.json())
# print(get_repsonse.text)
# print(get_repsonse.status_code)