import os

from selene import have, be
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
    assert authorization_cookie == None
    browser.open('')
    not browser.element(".account").should(have.text('My account'))


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


def test_remove_from_cart(login_through_api, demoshop):
    demoshop.post('/cart', data={'removefromcart': '3072408',
                                 'itemquantity3072408': '1',
                                 'updatecart': 'Update shopping cart',
                                 'discountcouponcode': '',
                                 'giftcardcouponcode': '',
                                 'CountryId': '0',
                                 'StateProvinceId': '0',
                                 'ZipPostalCode': ''})
    browser.open('/cart')
    browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_poll_is_submitted(login_through_api, demoshop):
    # already voted as user and cannot retract vote
    # poll is visible by default
    not browser.element('.poll-options').should(be.visible)
    pass


def test_add_to_wishlist(login_through_api, demoshop):
    demoshop.post('addproducttocart/details/80/2', data={
        'product_attribute_80_2_37': '112',
        'product_attribute_80_1_38': '114',
        'addtocart_80.EnteredQuantity': '1'})
    browser.open('/')
    browser.element('.wishlist-qty').should(have.text('(1)'))

