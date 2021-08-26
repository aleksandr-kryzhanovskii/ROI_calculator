from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class RoiCalculatorPage(Page):
    REGION_SELECT = (By.ID, 'regionSelect')
    TOTAL_FIELD_AREA = (By.ID, 'totalFieldArea')

    FORMS_SECTIONS = {
        'Information: Soil type': [
            (By.ID, 'loam'),
            (By.ID, 'Sandy'),
            (By.ID, 'Clayey'),
            (By.ID, 'Silty')
        ],
        'Information: Crop type': [
            (By.ID, 'CornSoy'),
            (By.ID, 'Cereal'),
            (By.ID, 'Vegetables'),
            (By.ID, 'Fruits'),
            (By.ID, 'Others')
        ],
        'Currently practicing: Tillage management': [
            (By.ID, 'fullTillage'),
            (By.ID, 'reducedTillage'),
            (By.ID, 'noTill')
        ],
        'Currently practicing: Cover crops': [
            (By.ID, 'No'),
            (By.ID, 'Yes')
        ],
        'Currently practicing: Nitrogen efficiency practices': [
            (By.ID, 'nitrogenEfficiencyPracticesNo'),
            (By.ID, 'nitrogenEfficiencyPracticesYes')
        ],
        'Willing to implement: Tillage management': [
            (By.ID, 'willingToImplementFullTillage'),
            (By.ID, 'willingToImplementReducedTillage'),
            (By.ID, 'willingToImplementNoTill')
        ],
        'Willing to implement: Cover crops': [
            (By.ID, 'willingToImplementCoverCropsNo'),
            (By.ID, 'willingToImplementCoverCropsYes')
        ],
        'Willing to implement: Type of cover crop': [
            (By.ID, 'willingToImplementCoverCropsTypeCerealsRye'),
            (By.ID, 'willingToImplementCoverCropsTypeLeguminose'),
            (By.ID, 'willingToImplementCoverCropsType2SpeciesMix'),
            (By.ID, 'willingToImplementCoverCropsTypeBrassica')
        ],
        'Willing to implement: Nitrogen efficiency practices': [
            (By.ID, 'willingToImplementNitrogenEfficiencyPracticesNo'),
            (By.ID, 'willingToImplementNitrogenEfficiencyPracticesYes')
        ]
    }

    NORTHERN_IA_SOUTHERN_MN = (By.CSS_SELECTOR, "option[value *= 'Region 1']")

    SHOW_TOTAL_BENEFITS = (By.ID, "submitForm")

    NO_RESULT_POPUP = (By.CSS_SELECTOR, 'div.no-result-body')
    RESULT_POPUP = (By.CSS_SELECTOR, 'div.calculator-result-body')
    # RESULT_POPUP = (By.ID, 'calculatorResult')

    SOIL_TIPE_TOOLTIP = (By.CSS_SELECTOR, "i svg") #?????#

    def open_calculator_page(self):
        self.open_url('https://us.agorocarbonalliance.com/farmers-advisors/#calculator')

    def input_total_field_area(self, search_query):
        self.input_text(search_query, *self.TOTAL_FIELD_AREA)

    def verify_input_result(self, search_query):
        #self.verify_text(search_query, *self.TOTAL_FIELD_AREA)
        current_value = self.find_element(*self.TOTAL_FIELD_AREA).get_attribute('value')
        assert current_value == search_query, f'Expected {search_query} but got {current_value}'

    def click_region_menu(self):
        self.click(*self.REGION_SELECT)

    def click_NorthernIA_SouthernMN(self):
        self.click(*self.NORTHERN_IA_SOUTHERN_MN)

    # def click_(self):
    #     self.click(*self.NORTHERN_IA_SOUTHERN_MN)

    def wait_submit_clickable(self):
        # self.wait_for_element_click(*self.SHOW_TOTAL_BENEFITS)
        self.click(*self.SHOW_TOTAL_BENEFITS)

    def click_show_total_benefits_btn(self):
        self.click(*self.SHOW_TOTAL_BENEFITS)

    def hover_total_area(self):
        total_area = self.find_elements(*self.TOTAL_FIELD_AREA)
        actions = ActionChains(self.driver)
        actions.move_to_element(total_area)
        actions.perform()

    def hover_soil_type_tooltip(self):
        total_area = self.find_elements(*self.SOIL_TIPE_TOOLTIP)
        actions = ActionChains(self.driver)
        actions.move_to_element(total_area)
        actions.perform()

    def verify_result_popup_open(self):
        self.find_element(*self.RESULT_POPUP)

    def verify_tag_type(self, value_type):
        current_value_type = self.find_element(*self.TOTAL_FIELD_AREA).get_attribute('type')
        assert value_type == current_value_type, f'Expected {value_type} but got {current_value_type}'

    def click_over_form_section(self, form_section):
        current_section = self.FORMS_SECTIONS[form_section]


        for current_option in current_section:
        #    print(current_option)
            self.click(*current_option)
