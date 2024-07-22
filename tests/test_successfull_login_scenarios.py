from playwright.sync_api import Page, expect
import pytest

test_data = [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
]


@pytest.mark.parametrize("username, password", test_data)
def test_valid_login_scenarios(page: Page, username: str, password: str) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=10000)
    expect(page.locator("[data-test='title']")).to_contain_text("Products")
