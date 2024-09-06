import requests

endpoint =  "http://127.0.0.1:8000/api"

get_repsonse = requests.get(endpoint, params={"ABC":123}, json="Hello world")

print(get_repsonse.json())
# print(get_repsonse.text)
# print(get_repsonse.status_code)