#We are using https://reqres.in for API test

import requests

url ="https://reqres.in/api/users?page=2"
response = requests.get(url)
#print(response)


#print(response.content)
#print(response.headers)

#Validate response code
assert response.status_code == 200

#Fetch response hearder

print(response.headers)
print(response.headers.get("Date"))
print(response.headers.get("Server"))

#Fetch cookies
print(response.cookies)

#Fetch elapse time
print(response.elapsed)

#print encoding
print(response.encoding)