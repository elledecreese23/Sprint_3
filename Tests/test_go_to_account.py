from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_3.locators import Locators
class Test_Go_from_To_Account:

    def test_switching_click_the_Constructor(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.form_for_filling))
        driver.find_element(*Locators.field_registration_login).send_keys('test1@yandex.ru')
        driver.find_element(*Locators.field_registration_password).send_keys('qazwsx4321')
        driver.find_element(*Locators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_exit))
        driver.find_element(*Locators. button_constructor).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.title_collect_burger))
        burger_link = driver.find_element(*Locators.title_collect_burger)
        assert burger_link.text == 'Соберите бургер', 'Название "Соберите бургер отображается "'

    def test_switching_click_the_logo_Stellar_Burgers(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.form_for_filling))
        driver.find_element(*Locators.field_registration_login).send_keys('test1@yandex.ru')
        driver.find_element(*Locators.field_registration_password).send_keys('qazwsx4321')
        driver.find_element(*Locators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_exit))
        driver.find_element(*Locators.button_stellar_burgers).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.title_collect_burger))
        burger_link = driver.find_element(*Locators.title_collect_burger)
        assert burger_link.text == 'Соберите бургер', 'Название "Соберите бургер отображается "'

    def test_check_history(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.form_for_filling))
        driver.find_element(*Locators.field_registration_login).send_keys('test1@yandex.ru')
        driver.find_element(*Locators.field_registration_password).send_keys('qazwsx4321')
        driver.find_element(*Locators.button_input).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.button_personal_account))
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.button_history_shop))
        history_shop = driver.find_element(*Locators.button_history_shop)
        assert history_shop.text == 'История заказов', "отображаться раздел 'История заказов'"