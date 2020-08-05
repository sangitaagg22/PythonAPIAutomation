#this is for authorization to https server
#pytest command to run the test pytest test_auth.py -s
#pytest to run specific test case pytest -k test_username_passwd_auth


import requests
from requests.auth import HTTPBasicAuth

def test_username_passwd_auth():
    url= "https://api.github.com/user"
    res=requests.get(url,auth=HTTPBasicAuth("username","passwd")) #it will take username and passwd
    print(res.text)