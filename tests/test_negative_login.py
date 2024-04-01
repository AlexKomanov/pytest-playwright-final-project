from playwright.sync_api import Page, expect
import pytest

testing_data = [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("", "", "Epic sadface: Username is required"),
    ("wrong_username", "", "Epic sadface: Password is required"),
    ("wrong_username", "wrong_password", "Epic sadface: Username and password do not match any user in this service")
]


@pytest.mark.parametrize("username, password, error_message", testing_data)
def test_not_valid_login_scenarios(page: Page, username: str, password: str, error_message: str) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text(error_message)
    expect(page).to_have_url('https://www.saucedemo.com/')
    page.wait_for_timeout(2000)


