import pytest
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login(page: Page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile(r".*inventory.html"))

    

@pytest.mark.parametrize("username,password,error_message", [
    ("standard_user", "wrong_password", "do not match"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("locked_out_user", "secret_sauce", "locked out"),
])
def test_invalid_login(page: Page, username, password, error_message):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(username, password)

    expect(login_page.error).to_contain_text(error_message)