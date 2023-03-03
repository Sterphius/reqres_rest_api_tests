import requests
from pytest_voluptuous import S
from schemas.single_user_schema import user_schema
from requests import Response

sample_user_data = {
    "name": "terry",
    "job": "captain"
}

patch_user_data = {
    "name": "matilda",
    "job": "cat"
}


def test_create_user():
    result: Response = requests.post('https://reqres.in/api/users/2', data=sample_user_data)

    assert result.status_code == 201
    assert result.json() == S(user_schema)


def test_patch_user():
    result: Response = requests.patch('https://reqres.in/api/users/2', data=patch_user_data)

    assert result.status_code == 200
    assert result.json() == S(user_schema)


def test_update_user():
    result: Response = requests.put('https://reqres.in/api/users/2', data=patch_user_data)

    assert result.status_code == 200
    assert result.json() == S(user_schema)


def test_delete_user():
    result: Response = requests.delete('https://reqres.in/api/users/2')

    assert result.status_code == 204

