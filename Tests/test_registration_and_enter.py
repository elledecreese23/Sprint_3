from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_3.locators import Locators


class Test_Regustration_and_login:

    def test_registration_and_enter_button_in_the_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.form_for_filling))
        driver.find_element(*Locators.button_input_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.form_for_filling))
        driver.find_element(*Locators.field_registration_login).send_keys('test1@yandex.ru')
        driver.find_element(*Locators.field_registration_password).send_keys('qazwsx4321')
        driver.find_element(*Locators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_place_an_order))
        order_button = driver.find_element(*Locators.button_place_an_order)
        assert order_button.text == 'Оформить заказ', 'Кнопка "Оформить" заказ  отображается после авторизации'

    def test_input_login_via_button_personal_account(self, driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.form_for_filling))
        driver.find_element(*Locators.field_registration_login).send_keys('test1@yandex.ru')
        driver.find_element(*Locators.field_registration_password).send_keys('qazwsx4321')
        driver.find_element(*Locators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_place_an_order))
        order_button = driver.find_element(*Locators.button_place_an_order)
        assert order_button.text == 'Оформить заказ', 'Кнопка "Оформить" заказ отображается после авторизации'

    def test_input_login_via_button_input_to_account(self, driver):
        driver.find_element(*Locators.button_input_to_account).click()
        driver.find_element(*Locators.field_registration_login).send_keys('test1@yandex.ru')
        driver.find_element(*Locators.field_registration_password).send_keys('qazwsx4321')
        driver.find_element(*Locators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_place_an_order))
        order_button = driver.find_element(*Locators.button_place_an_order)
        assert order_button.text == 'Оформить заказ', 'Кнопка "Оформить" заказ отображается после авторизации'

    def test_input_login_via_password_recovery_button(self, driver):
        driver.find_element(*Locators.button_input_to_account).click()
        driver.find_element(*Locators.return_password).click()
        driver.find_element(*Locators.button_input_return_password).click()
        driver.find_element(*Locators.field_registration_login).send_keys('test1@yandex.ru')
        driver.find_element(*Locators.field_registration_password).send_keys('qazwsx4321')
        driver.find_element(*Locators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.button_place_an_order))
        order_button = driver.find_element(*Locators.button_place_an_order)
        assert order_button.text == 'Оформить заказ', 'Кнопка "Оформить" отображается после авторизации'

    def test_registration_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.title_entry))
        driver.find_element(*Locators.field_registration_name).send_keys("Dmitrii11")
        driver.find_element(*Locators.field_registration_login).send_keys("test_uzer001@gmail.com")
        driver.find_element(*Locators.field_registration_password).send_keys("Qazwsx4321")
        driver.find_element(*Locators.button_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.title_entry))
        assert 'Регистрация' in driver.find_element(*Locators.title_entry).text, "После успешной регистрации отображается заголовок Вход"

    def test_registration_entering_a_password_of_3_symbols(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*Locators.field_registration_name).send_keys("Dmitrii")
        driver.find_element(*Locators.field_registration_login).send_keys("test@yandexx.ru")
        password_locator = driver.find_element(*Locators.field_registration_password)
        password_locator.send_keys('777')
        assert len(password_locator.get_attribute('value')) <= 6, "Пароль меньше 6 символов"