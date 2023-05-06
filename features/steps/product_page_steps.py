from behave import given, when, then


@given('Open Product Details page')
def open_product_page(context):
    context.app.product_page.open_product_page()


@when('Click to add product to cart')
def add_to_cart(context):
    context.app.product_page.add_to_cart()


@when('Verify {text} confirmation is shown')
def verify_cart_confirm(context, text):
    context.app.product_page.verify_cart_confirm(text)


@when('Click "View my cart"')
def view_my_cart(context):
    context.app.product_page.view_my_cart()


@then('Verify {text} is visible')
def verify_cart_page(context, text):
    context.app.product_page.verify_cart_page(text)