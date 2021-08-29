from behave import then, given, when
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@given('Open calculator page')
def open_roi_calculator(context):
   context.app.roi_calculator_page.open_calculator_page()


@when('Click Total Benefits button')
def click_show_total_benefits_btn(context):
    context.app.roi_calculator_page.click_show_total_benefits_btn()



@when('Enter {search_query} into input field')
def input_total_field_area(context, search_query):
    context.app.roi_calculator_page.input_total_field_area(search_query)


@when('Click on Region Menu')
def click_region_menu(context):
   context.app.roi_calculator_page.click_region_menu()


@when('Click on Northern IA/Southern MN Region')
def click_NorthernIA_SouthernMN(context):
   context.app.roi_calculator_page.click_NorthernIA_SouthernMN()

@then('Verify {expected_query} was added')
def click_input_result(context, expected_query):
   context.app.roi_calculator_page.verify_input_result(expected_query)


@then('Verify User can see the result popup')
def verify_result_popup_open(context):
   context.app.roi_calculator_page.verify_result_popup_open()


@when('Hover over Soil type tooltip')
def hover_over_soil_type_tooltip(context):
   context.app.roi_calculator_page.hover_soil_type_tooltip()

@when('Click Fruits crop type')
def click_NorthernIA_SouthernMN(context):
   context.app.roi_calculator_page.click_fruits()

@then('click over form {form_section} section')
def click_over_options(context, form_section):
   sleep(4)
   context.app.roi_calculator_page.click_over_form_section(form_section)

# @then('Verify User can see tooltips text')
# def click_(context):
#    context.app.roi_calculator_page.()
TOTAL_FIELD_AREA = (By.ID, 'totalFieldArea')

@then('Verify letters was NOT added to search field')
def verify_not_negativ(context):
   e = context.driver.find_element(*TOTAL_FIELD_AREA)
   assert e == int, f'Input data is not an integer'

@then('Verify 0 was NOT added to search field')
def verify_not_negativ(context):
   e = context.driver.find_element(*TOTAL_FIELD_AREA)
   assert e == 0, f'Input data CAN NOT be 0'

@then('Verify symbol was NOT added to search field')
def verify_not_negativ(context):
   e = context.driver.find_element(*TOTAL_FIELD_AREA)
   assert e != int, f'Input data is not an integer'