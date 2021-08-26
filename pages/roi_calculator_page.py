from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

class RoiCalculatorPage(Page):
    REGION_SELECT = (By.ID, 'regionSelect')
    TOTAL_FIELD_AREA = (By.ID, 'totalFieldArea')
    LOAM = (By.ID, 'Sandy')
    CLAYEY = (By.ID, 'Clayey')

    CORN_SOY = (By.ID, 'CornSoy')
    CEREAL = (By.ID, 'Cereal')
    VEGETABLES = (By.ID, 'Vegetables')
    FRUITS = (By.ID, 'Fruits')
    OTHERS = (By.ID, 'Others')

    FULL_TILLAGE = (By.ID, 'fullTillage')
    NO_TILL = (By.ID, 'noTill')
    REDUCED_TILLAGE = (By.ID, 'reducedTillage')

    COVER_CORPS_NO = (By.ID, 'willingToImplementCoverCropsNo')
    COVER_CORPS_YES = (By.ID, 'willingToImplementCoverCropsYes')

    COVER_CORPS_CEREALS_RYE = (By.ID, 'willingToImplementCoverCropsTypeCerealsRye')
    COVER_CORPS_LEGUMINOSE = (By.ID, 'willingToImplementCoverCropsTypeLeguminose')
    COVER_CORPS_2_SPECIES_MIX = (By.ID, 'willingToImplementCoverCropsType2SpeciesMix')
    COVER_CORPS_2_BRASSICA = (By.ID, 'willingToImplementCoverCropsTypeBrassica')

    NITROGEN_EFFICIENCY_PRACTICE_NO = (By.ID, 'willingToImplementNitrogenEfficiencyPracticesNo')
    NITROGEN_EFFICIENCY_PRACTICE_YES = (By.ID, 'willingToImplementNitrogenEfficiencyPracticesYes')

    NORTHERN_IA_SOUTHERN_MN = (By.CSS_SELECTOR, "option[value *= 'Region 1']")

    SHOW_TOTAL_BENEFITS = (By.XPATH, "//button[@type='submit']")

    NO_RESULT_POPUP = (By.ID, 'calculatorNoResultContactUs')
    RESULT_POPUP = (By.CSS_SELECTOR, 'th.d-lg-none')

    SOIL_TIPE_TOOLTIP = (By.CSS_SELECTOR, "i[data-original-title*='soil type']")

    FORMS_SECTIONS = {
        'Information: Soil type': [
            (By.ID, 'Loam'),
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
        self.submit(*self.SHOW_TOTAL_BENEFITS)


    def click_fruits(self):
        self.click(*self.FRUITS)


    def hover_soil_type_tooltip(self):
        total_area = self.find_elements(*self.SOIL_TIPE_TOOLTIP)
        actions = ActionChains(self.driver)
        actions.move_to_element(total_area)
        actions.perform()


    def verify_result_popup_open(self):
        self.find_element(*self.RESULT_POPUP)

    def click_over_form_section(self, form_section):
        current_section = self.FORMS_SECTIONS[form_section]

        for current_option in current_section:
            #print(current_option)
            #self.wait_for_element_click(*current_option)
            #e = self.driver.find_element(By.ID, 'Sandy')
            #print('clicking..')
            #e.click()
            self.wait_for_element_click(*current_option)





