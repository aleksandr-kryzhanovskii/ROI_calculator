from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)


    def click(self, *locator):
        e = self.find_element(*locator)
        e.click()



    def submit(self, *locator):
        self.driver.find_element(*locator).submit()

    def wait_for_element_click(self, *locator):
        print(locator)
        print(type(locator))
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_until_element_dissapeare(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_until_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_url(self, url,):
        self.driver.get(url)

    def verify_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text} but get {actual_text}'

    def verify_url_contains_querty(self, querty):
        assert querty in self.driver.current_url, f'{querty} not in {self.driver.current_url}'

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def scroll_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)
