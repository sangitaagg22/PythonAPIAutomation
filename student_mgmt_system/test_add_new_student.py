#Below test cases test the API from nhttps://www.thetestingworldapi.com/Help
#Pytest - k <test file name> -s used to print the statement.

import requests
import json
import pytest,jsonpath

url = "https://www.thetestingworldapi.com/api/studentsDetails"

'''res=requests.get(url,verify=False)
print(res.status_code)
print(res.text)'''


@pytest.mark.skip
def test_add_new_students():
    url = "https://www.thetestingworldapi.com/api/studentsDetails"
    student_info='{"first_name": "sample string 2","middle_name": "sample string 3","last_name": "sample string 4", "date_of_birth": "sample string 5"}'
    json_data = json.loads(student_info)
    res= requests.post(url,data=json_data,verify=False)
    print(res.status_code)
    print(res.text)

@pytest.mark.skip
def test_get_student_details():
    url= "https://www.thetestingworldapi.com/api/studentsDetails/57301"
    res=requests.get(url,verify=False)
    print(res.text)
    json_res=json.loads(res.text)
    id= jsonpath.jsonpath(json_res,"data.id")  #always return list
    print(id[0])
    assert id[0]==57301


def test_update_new_students():
    url = "https://www.thetestingworldapi.com/api/studentsDetails/57301"
    student_info='{"id": 57301, "first_name": "ritu","middle_name": "kumar","last_name": "sample string 4", "date_of_birth": "sample string 5"}'
    json_data = json.loads(student_info)
    res= requests.put(url,data=json_data,verify=False)
    print(res.status_code)
    print(res.text)
    assert res.status_code==200

def test_delete_students():
    url = "https://www.thetestingworldapi.com/api/studentsDetails/57301"
    res=requests.delete(url,verify=False)
    print(res.text)


