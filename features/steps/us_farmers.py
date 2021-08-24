from behave import then, given, when
from time import sleep


@given('Open Agoro carbon alliance page')
def open_main_page(context):
   context.app.main_page.open_main_page()

@when('Scroll down to calculator section')
def scroll_to_calculator(context):
    context.app.main_page.scroll_to_calculator()
    sleep(4)


@when('Hover over Farmers/Edvisors link')
def hover_total_area(context):
   context.app.main_page.hover_total_area()

@when('Click U.S. Farmers link')
def click_us_farmers(context):
   context.app.main_page.click_us_farmers()



