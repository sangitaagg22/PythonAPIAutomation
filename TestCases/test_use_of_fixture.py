#Below test cases are dummy test to understand pytest framework
#It willl make the group so that user can execute the group of test by using command pytest -m smoke or pytest -m sanity

import json
import requests
import pytest


@pytest.fixture(scope="module") #if we specify the scope then it will execute only once in whole module
def start_exec():  #it will execute only in the begning of test cases
    global url
    url = "https://reqres.in/api/users"

@pytest.mark.smoke()
def test_smoke_user(setup):

    string = '{"name": "david","job": "manager"}'
    json_obj=json.loads(string)

    print(json_obj)

    req = requests.post(url,data=json_obj)  #return 201
    print(req.status_code)
    assert req.status_code==201

@pytest.mark.smoke()
def test_smoke_other_user(setup):

    string = '{"name": "david","job": "manager"}'
    json_obj=json.loads(string)

    print(json_obj)

    req = requests.post(url,data=json_obj)  #return 201
    print(req.status_code)
    assert req.status_code==201
