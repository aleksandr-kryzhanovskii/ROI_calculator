from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class RoiCalculatorPage(Page):
    REGION_SELECT = (By.ID, 'regionSelect')
    TOTAL_FIELD_AREA = (By.ID, 'totalFieldArea')





    NORTHERN_IA_SOUTHERN_MN = (By.CSS_SELECTOR, "option[value *= 'Region 1']")

    SHOW_TOTAL_BENEFITS = (By.ID, "submitForm")

    NO_RESULT_POPUP = (By.XPATH, "//div[@class='no-result-body']/p")

    RESULT_POPUP = (By.XPATH, "//div[@class='calculator-result-body']/h3")

    SOIL_TIPE_TOOLTIP = (By.CSS_SELECTOR, "i[data-original-title*='soil type']")
    TOOL = (By.CSS_SELECTOR, "i[data-original-title*='soil type']")
    TOOL_2 = (By.CSS_SELECTOR, "i[data-original-title*='Nitrogen efficiency practices']")

    FORMS_SECTIONS = {
        'Information: Soil type': [
            (By.XPATH, '//label[@for="Loam"]'),
            (By.XPATH, '//label[@for="Sandy"]'),
            (By.XPATH, '//label[@for="Clayey"]'),
            (By.XPATH, '//label[@for="Silty"]')
        ],
        'Information: Crop type': [
            (By.XPATH, '//label[@for="CornSoy"]'),
            (By.XPATH, '//label[@for="Cereal"]'),
            (By.XPATH, '//label[@for="Vegetables"]'),
            (By.XPATH, '//label[@for="Fruits"]'),
            (By.XPATH, '//label[@for="Others"]')
        ],
        'Currently practicing: Tillage management': [
            (By.XPATH, '//label[@for="fullTillage"]'),
            (By.XPATH, '//label[@for="reducedTillage"]'),
            (By.XPATH, '//label[@for="noTill"]')
        ],
        'Currently practicing: Cover crops': [
            (By.XPATH, '//label[@for="No"]'),
            (By.XPATH, '//label[@for="Yes"]')
        ],
        'Currently practicing: Nitrogen efficiency practices': [
            (By.XPATH, '//label[@for="nitrogenEfficiencyPracticesYes"]'),
            (By.XPATH, '//label[@for="nitrogenEfficiencyPracticesNo"]')
        ],
        'Willing to implement: Tillage management': [
            (By.XPATH, '//label[@for="willingToImplementFullTillage"]'),
            (By.XPATH, '//label[@for="willingToImplementReducedTillage"]'),
            (By.XPATH, '//label[@for="willingToImplementNoTill"]')
        ],
        'Willing to implement: Cover crops': [
            (By.XPATH, '//label[@for="willingToImplementCoverCropsYes"]'),
            (By.XPATH, '//label[@for="willingToImplementCoverCropsNo"]')
        ],
        'Willing to implement: Type of cover crop': [
            (By.XPATH, '//label[@for="willingToImplementCoverCropsTypeCerealsRye"]'),
            (By.XPATH, '//label[@for="willingToImplementCoverCropsTypeLeguminose"]'),
            (By.XPATH, '//label[@for="willingToImplementCoverCropsType2SpeciesMix"]'),
            (By.XPATH, '//label[@for="willingToImplementCoverCropsTypeBrassica"]')
        ],
        'Willing to implement: Nitrogen efficiency practices': [
            (By.XPATH, '//label[@for="willingToImplementNitrogenEfficiencyPracticesNo"]'),
            (By.XPATH, '//label[@for="willingToImplementNitrogenEfficiencyPracticesYes"]')
        ]
    }

    REGION = {
        'Region name: Northern IA/Southern MN Region':
            (By.CSS_SELECTOR, "option[value *= 'Region 1']"),
        'Region name: Southern IA/Northern MO':
            (By.CSS_SELECTOR, "option[value *= 'Region 2']"),

    }


    TOOL_TIPS = {
        'Information': [
            (By.CSS_SELECTOR, "i[data-original-title*='soil type']"),
            (By.CSS_SELECTOR,"i[data-original-title*='crop type']")
        ],

        'Currently practicing': [

        ],

        'Willing to implement': [
            (By.CSS_SELECTOR, "i[data-original-title*='Nitrogen practices']")
        ]

    }




    def open_calculator_page(self):
        self.open_url('https://us.agorocarbonalliance.com/farmers-advisors/#calculator')


    def input_total_field_area(self, search_query):
        self.input_text(search_query, *self.TOTAL_FIELD_AREA)

    def verify_input_result(self, search_query):
        current_value = self.find_element(*self.TOTAL_FIELD_AREA).get_attribute('value')
        assert current_value == search_query, f'Expected {search_query} but got {current_value}'

    def click_region_menu(self):
        self.click(*self.REGION_SELECT)

    def click_NorthernIA_SouthernMN(self):
        self.click(*self.NORTHERN_IA_SOUTHERN_MN)

    # def click_(self):
    #     self.click(*self.NORTHERN_IA_SOUTHERN_MN)

    def wait_submit_clickable(self):
        self.wait_for_element_click(*self.SHOW_TOTAL_BENEFITS)


    def click_show_total_benefits_btn(self):
        print('kasdf')
        self.find_element(*self.SHOW_TOTAL_BENEFITS).submit()
        sleep(3)
        #self.click(*self.SHOW_TOTAL_BENEFITS)


    def click_fruits(self):
        self.click(*self.FRUITS)


    def hover_soil_type_tooltip(self):
        total_area = self.find_element(*self.TOOL)
        total_area.location_once_scrolled_into_view
        #self.driver.execute_script("window.scrollTo(0, window.scrollY + 600)")
        #sleep(3)
        actions = ActionChains(self.driver)
        actions.move_to_element(total_area)
        actions.perform()

    SCROLL = (By.XPATH, '//label[@for="willingToImplementCoverCropsTypeCerealsRye"]')

    SCROLL_2 = (By.ID, "lp-code-19")

    SCROLL_3 = (By.XPATH, "//div[@class='col-12 col-lg-8']/nav/p")


    def scroll(self):
        area = self.find_element(*self.SCROLL_3)
        self.scroll_to_element(*self.SCROLL_3)
        # area.location_once_scrolled_into_view



    def verify_result_popup_open(self):
        sleep(2)
        expected_text = "Projected average annual benefit over 10 years*"
        actual_text = self.find_element(*self.RESULT_POPUP).text
        assert expected_text == actual_text, f'Expected {expected_text} but get {actual_text}'


    def click_over_form_section(self, form_section):
        current_section = self.FORMS_SECTIONS[form_section]
        if ("Willing to implement" in form_section) or ("Currently practicing" in form_section):
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 600)")
            sleep(3)
        for current_option in current_section:
            ele = self.find_element(*current_option)
            ele.click()


    def click_over_region_section(self, region):
        current_region = self.REGION[region]
        ele = self.find_element(*current_region)
        ele.click()
        sleep(4)

    def verify_attribute(self, attribute):
        current_value = self.find_element(*self.TOTAL_FIELD_AREA).get_attribute('type')
        assert current_value == attribute, f'Expected {attribute} but got {current_value}'


    def hover_over_section(self, section):
        tooltips_locator = self.TOOL_TIPS[section]
        print('locators', tooltips_locator)

        if 'Willing to implement' in section:
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 600)")
            sleep(10)


        #actions = ActionChains(self.driver)


        for locator in tooltips_locator:

            tooltip = self.find_element(*locator)

            #actions.move_to_element(tooltip)
            #actions.perform()
            sleep(3)