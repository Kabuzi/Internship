from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Click on search icon')
def click_search_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT))
    context.driver.find_element(*SEARCH_SUBMIT).click()
    #sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"



@when('Click on the first product')
def verify_search_result(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Product image is missing'
        product_tile = product.find_element(*PRODUCT_TITLE).text
        assert product_tile, 'Product title is missing'