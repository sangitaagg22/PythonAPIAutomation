import requests
import jsonpath
import json

url= "https://reqres.in/api/users?page=2"

res= requests.get(url)

assert res.status_code== 200
#print(res.text )

json_obj =json.loads(res.text)

for i in range(0,3):
    firstname= jsonpath.jsonpath(json_obj,'data['+str(i)+'].first_name')  #it returns list
    print(firstname[0])


