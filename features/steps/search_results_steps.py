from behave import given, when, then


@given('Open search result "cure" page')
def open_search_result_cure(context):
    context.app.search_results_page.open_search_result_cure()


@when('Click on CureSkin logo in the header')
def click_logo_header(context):
    context.app.search_results_page.click_logo_header()


@then('Verify user is taken to {text}')
def verify_on_main_page(context, text):
    context.app.search_results_page.verify_on_main_page(text)


@then('Verify that {text}')
def verify_23_products(context, text):
    context.app.search_results_page.verify_23_products(text)


