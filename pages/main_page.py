from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(Page):
    FARMERS_EDVISORS = (By.CSS_SELECTOR, "ul[role='list'] a[href ='/farmers-advisors/']")
    US_FARMERS = (By.CSS_SELECTOR, "a[href='https://us.agorocarbonalliance.com/farmers-advisors']")
    MY_FARM_INFORMATION = (By.CSS_SELECTOR, "#myFarmInformation h3")
    TEST = (By.CSS_SELECTOR, "span.testimonial-item-name")

    def open_main_page(self):
        self.open_url('https://agorocarbonalliance.com/')


    def hover_total_area(self):
        total_area = self.find_elements(*self.FARMERS_EDVISORS)
        actions = ActionChains(self.driver)
        actions.move_to_element(total_area)
        actions.perform()

    def click_us_farmers(self):
        self.click(*self.US_FARMERS)

    def scroll_to_calculator(self):
        self.scroll_to_element(*self.TEST)

    # def scroll_to_calculator(self):
    #     self.scroll_to_element(*self.MY_FARM_INFORMATION)



