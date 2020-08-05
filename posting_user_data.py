import json
import requests

url = "https://reqres.in/api/users"
string = '{"name": "david","job": "manager"}'
json_obj=json.loads(string)

print(json_obj)

requests = requests.post(url,data=json_obj)  #return 201
print(requests.status_code)