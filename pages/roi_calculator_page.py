from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


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

    SHOW_TOTAL_BENEFITS = (By.CSS_SELECTOR, "button[type='submit'] svg") #??????#

    NO_RESULT_POPUP = (By.CSS_SELECTOR, 'div.no-result-body')
    RESULT_POPUP = (By.CSS_SELECTOR, 'div.calculator-result-body')

    SOIL_TIPE_TOOLTIP = (By.CSS_SELECTOR, "i svg") #?????#

    def open_calculator_page(self):
        self.open_url('https://us.agorocarbonalliance.com/farmers-advisors/#calculator')

    def input_total_field_area(self, search_query):
        self.input_text(search_query, *self.TOTAL_FIELD_AREA)

    def verify_input_result(self, search_query):
        self.verify_text(search_query, *self.TOTAL_FIELD_AREA)

    def click_region_menu(self):
        self.click(*self.REGION_SELECT)

    def click_NorthernIA_SouthernMN(self):
        self.click(*self.NORTHERN_IA_SOUTHERN_MN)

    # def click_(self):
    #     self.click(*self.NORTHERN_IA_SOUTHERN_MN)

    def wait_submit_clickable(self):
        self.wait_for_element_click(*self.SHOW_TOTAL_BENEFITS)


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




