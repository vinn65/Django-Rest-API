import requests
from getpass import getpass

auth_endpoint =  "http://127.0.0.1:8000/auth/"
username = input("What is your username:\n")
password = getpass("Enter password:\n")
auth_response = requests.post(auth_endpoint, json={
    'username': username, 'password': password
})

print(auth_response.json())
if auth_response == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization":f"Bearer {token} "
    }
    endpoint =  "http://127.0.0.1:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())
