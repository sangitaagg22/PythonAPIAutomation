#Use PUT method for updating the content

import json
import requests

url = "https://reqres.in/api/users"
string = '{"name": "david","job": "sdet"}'
json_obj=json.loads(string)

print(json_obj)

requests = requests.put(url,data=json_obj)  #return 200
print(requests.status_code)

