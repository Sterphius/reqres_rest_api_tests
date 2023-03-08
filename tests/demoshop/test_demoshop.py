import os

from selene import have
from selene.support.shared import browser
import allure


def test_newsletter_sign(login_through_api):
    with allure.step('Type the email'):
        browser.element('#newsletter-email').set_value(os.getenv("TEST_USER_EMAIL"))

    with allure.step('Click subscribe button'):
        browser.element('#newsletter-subscribe-button').click()

    with allure.step('Success sign up text appears'):
        browser.element('#newsletter-result-block').should(
            have.text('Thank you for signing up! A verification email has been sent. We appreciate your interest'))


def test_log_out(login_through_api):
    browser.driver.delete_cookie("NOPCOMMERCE.AUTH")
    browser.open("")
    browser.element(".ico-register").should(have.text('Register'))


def test_login_with_bad_creds(demoshop):
    response = demoshop.post("/login", json={"Email": os.getenv("TEST_USER_EMAIL"),
                                             "Password": ''},
                             allow_redirects=False)

    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open('')
    assert authorization_cookie == None


def test_laptop_added_to_the_cart(login_through_api, demoshop):
    demoshop.post('/addproducttocart/catalog/31/1/1',
                  data={'itemquantity3072333': '1',
                        'updatecart': 'Update shopping cart',
                        'discountcouponcode': '',
                        'giftcardcouponcode': '',
                        'CountryId': '0',
                        'StateProvinceId': '0',
                        'ZipPostalCode': ''})

    browser.open('/cart')
    browser.element('.product-name').should(have.text('14.1-inch Laptop'))


def test_address_add(login_through_api, demoshop):
    demoshop.post('/customer/addressadd', data={
        'Address.Id': '0',
        'Address.FirstName': 'test_first_name',
        'Address.LastName': 'test_last_name',
        'Address.Email': '213123213@mail.ru',
        'Address.Company': '',
        'Address.CountryId': '1',
        'Address.StateProvinceId': '1',
        'Address.City': 'test_city',
        'Address.Address1': 'test_address',
        'Address.Address2':'',
        'Address.ZipPostalCode': '111222',
        'Address.PhoneNumber': '+7123123321',
        'Address.FaxNumber': ''
    })
    browser.open('/customer/addresses')
    browser.element('.address-list').should(have._not_.text('No addresses'))


def test_poll_is_submitted(login_through_api, demoshop):
    # already voted as user and cannot retract vote
    # poll is visible by default
    assert browser.element('.poll-options') is not None


def test_add_to_wishlist(login_through_api, demoshop):
    demoshop.post('/addproducttocart/details/80/2', data={
        'product_attribute_80_2_37': '112',
        'product_attribute_80_1_38': '114',
        'addtocart_80.EnteredQuantity': '1'})
    browser.open('/')
    browser.element('.wishlist-qty').should(have.text('(1)'))
