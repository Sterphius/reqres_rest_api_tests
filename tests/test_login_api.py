import requests
from pytest_voluptuous import S
from schemas.login_schema import login_schema, error_schema
from requests import Response

some_user = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

user_wo_pass = {
    "email": "test_mail@gmail.com"
}


def test_success_login():
    result: Response = requests.post('https://reqres.in/api/login', data=some_user)

    assert result.status_code == 200
    assert result.json() == S(login_schema)


def test_unsuccess_login():
    result: Response = requests.post('https://reqres.in/api/login', data=user_wo_pass)

    assert result.status_code == 400
    assert result.json() == S(error_schema)
