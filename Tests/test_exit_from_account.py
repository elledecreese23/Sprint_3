from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_3.locators import Locators

class Test_exit_from_account():
    def test_log_out_log_out_from_account(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.form_for_filling))
        driver.find_element(*Locators.field_registration_login).send_keys('test1@yandex.ru')
        driver.find_element(*Locators.field_registration_password).send_keys('qazwsx4321')
        driver.find_element(*Locators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_exit))
        driver.find_element(*Locators.button_exit).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.title_entry))
        assert driver.find_element(*Locators.title_entry).text == 'Вход', 'После выхода из аккаунта отображается заголовок "Вход"'