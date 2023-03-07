import os
import pytest
from selene.support.shared import browser
from selene.support.conditions import have
from utils.base_session import BaseSession
from allure import step
from dotenv import load_dotenv

load_dotenv()

browser.config.base_url = os.getenv("DEMOSHOP_WEB_URL")


@pytest.fixture(scope="session")
def demoshop():
    demoshop_api_url = os.getenv("DEMOSHOP_API_URL")
    return BaseSession(demoshop_api_url)


@pytest.fixture(scope='function')
def login_through_api(demoshop):
    response = demoshop.post("/login", json={"Email": os.getenv("TEST_USER_EMAIL"),
                                             "Password": os.getenv("TEST_USER_PASSWORD")},
                             allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("/Themes/DefaultClean/Content/images/logo.png")

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    browser.open("")

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(os.getenv("TEST_USER_EMAIL")))

    return browser


@pytest.fixture(scope="session")
def reqres():
    reqres_api_url = os.getenv("REQRES_API_URL")
    return BaseSession(reqres_api_url)
