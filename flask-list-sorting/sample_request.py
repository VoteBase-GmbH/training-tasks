import json
import requests

## This is a sample request to test the api endpoint.

new_headers = {'Content-type': 'application/json'}

url = 'http://localhost:5000/sort'

req_num = json.dumps([1, 2, 3, 6, 90, 8, 7, 10, 0, 67, 200, 100, -1])
print('Request: ', req_num)

response = requests.post(url, req_num, headers=new_headers)
sorted_numbers = response.json()

print('Response Status: ', response.status_code)
print('Sorted numbers: ', sorted_numbers)
