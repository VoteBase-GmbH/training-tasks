import requests
import json

url = "http://127.0.0.1:5000/"

int_list = [8,7,2,10,200,39,44,12,18,22]

response = requests.post(url, data = {"list_of_numbers": json.dumps(int_list)})
print(response.json())