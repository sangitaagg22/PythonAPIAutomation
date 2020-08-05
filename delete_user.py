import requests


url = "https://reqres.in/api/users/2"

res= requests.delete(url)
print(res.status_code)  #delete will return 204

assert  res.status_code ==204

