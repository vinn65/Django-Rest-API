import requests

key = input("Enter key to delete:")
key = int(key)
print(key)
endpoint =  "http://127.0.0.1:8000/api/products/{key}/delete/"

get_response = requests.delete(endpoint)

print(get_response.status_code)