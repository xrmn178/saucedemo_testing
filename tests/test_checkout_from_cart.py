import re 
from playwright.sync_api import Playwright, sync_playwright, expect 
 
def test_checkout_from_cart(playwright: Playwright) -> None: 
    try: 
        browser = playwright.chromium.launch(headless=False) 
        context = browser.new_context() 
        page = context.new_page() 
        page.goto("https://www.saucedemo.com/") 
        page.locator("[data-test=\"username\"]").click() 
        page.locator("[data-test=\"username\"]").fill("standard_user") 
        page.locator("[data-test=\"password\"]").click() 
        page.locator("[data-test=\"password\"]").fill("secret_sauce") 
        page.locator("[data-test=\"login-button\"]").click() 
        page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click() 
        page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click() 
        page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click() 
        page.locator("a").filter(has_text="3").click() 
        page.locator("[data-test=\"checkout\"]").click() 
        page.locator("[data-test=\"firstName\"]").click() 
        page.locator("[data-test=\"firstName\"]").fill("") 
        page.locator("[data-test=\"firstName\"]").click() 
        page.locator("[data-test=\"firstName\"]").click() 
        page.locator("[data-test=\"firstName\"]").fill("First Name") 
        page.locator("[data-test=\"lastName\"]").click() 
        page.locator("[data-test=\"lastName\"]").fill("Last Name") 
        page.locator("[data-test=\"postalCode\"]").click() 
        page.locator("[data-test=\"postalCode\"]").fill("123") 
        page.locator("[data-test=\"continue\"]").click() 
        page.locator("[data-test=\"finish\"]").click() 
 
        locator = page.locator("h2.complete-header") 
        expect(locator).to_have_text(re.compile(r"Thank you for your order!")) 
 
        context.close() 
        browser.close() 
        print("Тест успешно выполнен!") 
    except Exception as e: 
        print(f"Произошла ошибка: {str(e)}") 
 
with sync_playwright() as playwright: 
    test_checkout_from_cart(playwright)
