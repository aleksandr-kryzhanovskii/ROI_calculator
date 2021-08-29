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

    SHOW_TOTAL_BENEFITS = (By.ID, "submitForm")

    NO_RESULT_POPUP = (By.XPATH, "//div[@class='no-result-body']/p")

    RESULT_POPUP = (By.XPATH, "//div[@class='calculator-result-body']/h3")

    SOIL_TIPE_TOOLTIP = (By.CSS_SELECTOR, "i[data-original-title*='soil type']")
    TOOL = (By.CSS_SELECTOR, "i[data-original-title*='soil type']")

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
            (By.XPATH, '//label[@for="No"]'),
            (By.XPATH, '//label[@for="No"]')
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
            (By.XPATH, '//label[@for="wwillingToImplementNitrogenEfficiencyPracticesNo"]'),
            (By.XPATH, '//label[@for="wwillingToImplementNitrogenEfficiencyPracticesYes"]')
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
        total_area = self.find_element(*self.SOIL_TIPE_TOOLTIP)
        total_area.location_once_scrolled_into_view
        sleep(3)
        actions = ActionChains(self.driver)
        actions.move_to_element(total_area)
        actions.perform()

    SCROLL = (By.XPATH, '//label[@for="willingToImplementCoverCropsTypeCerealsRye"]')

    SCROLL_2 = (By.ID, "lp-code-19")

    SCROLL_3 = (By.XPATH, "//div[@class='col-12 col-lg-8']/nav/p")


    def scroll(self):
        area = self.find_element(*self.SCROLL_3)
        area.location_once_scrolled_into_view



    def verify_result_popup_open(self):
        sleep(2)
        expected_text = "Projected average annual benefit over 10 years*"
        actual_text = self.find_element(*self.RESULT_POPUP).text
        assert expected_text == actual_text, f'Expected {expected_text} but get {actual_text}'
        # GEt the TExt into a variable
        #assert exp == actual

    def click_over_form_section(self, form_section):
        current_section = self.FORMS_SECTIONS[form_section]

        for current_option in current_section:
            self.find_element(*current_option).click()







