import json
import requests
import pytest

a=10
@pytest.mark.skipif(a>10,reason="a is greater than 10")   #skip on the basis of condition
def test_user():
    url = "https://reqres.in/api/users"
    string = '{"name": "david","job": "manager"}'
    json_obj=json.loads(string)

    print(json_obj)

    req = requests.post(url,data=json_obj)  #return 201
    print(req.status_code)
    assert req.status_code==202

@pytest.mark.skip("I am skipping this test case") #skip without condition
def test_other_user():
    url = "https://reqres.in/api/users"
    string = '{"name": "david","job": "manager"}'
    json_obj=json.loads(string)

    print(json_obj)

    req = requests.post(url,data=json_obj)  #return 201
    print(req.status_code)
    assert req.status_code==202

@pytest.mark.sanity  # to make group, run the group of test cases with the sanity test
def test_get_user_data():
    url = "https://reqres.in/api/users"
    res = requests.get(url)
    assert res.status_code == 200

@pytest.mark.smoke #to run the group of test cases with the smoke test
def test_get_user_data():
    url = "https://reqres.in/api/users"
    res = requests.get(url)
    assert res.status_code == 200

@pytest.mark.sanity
def test_delete_user_data():
    url = "https://reqres.in/api/users/2"

    res = requests.delete(url)
    print(res.status_code)  # delete will return 204

    assert res.status_code == 204
