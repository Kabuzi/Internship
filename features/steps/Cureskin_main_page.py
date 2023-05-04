from behave import given, when, then


@given('Open Cureskin main page')
def open_cureskin(context):
    context.app.main_page.open_main()


@when('close popup')
def close_popup(context):
    context.app.header.click_popup()


@when('input {product} into search field')
def search_for_item(context, product):
    context.app.header.input_search_text(product)


@when('click on search field')
def click_search_field(context):
    context.app.header.click_search_field()


@when('Click on search')
def click_on_search(context):
    context.app.header.click_search()


@then('Verify {items} results for cure are shown')
def verify_items(context, items):
    context.app.search_results_page.find_items(items)

