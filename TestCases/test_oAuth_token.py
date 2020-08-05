"""
Sometime to access the api, user send the username and password and on the bais of that authorization took place
thorugh which user can access the api.
Below is dummy program

"""

import requests
import jsonpath


def test_oAuth_auth_token():
    token_url_data= "http://thetestingworldapi.com/Token"
    data={'grant_type':'password','username':'admin','password':'password'}
    res= requests.post(token_url_data)
    token_value=jsonpath.jsonpath(res.json(),'access_token')
    auth={'Authorization' : 'Bearer '+token_value[0]}
    API_URL= 'http://thetestingworldapi.com/api/StDetails/1104'
    res= requests.get(API_URL,hearders=auth)
    print(res.text)




