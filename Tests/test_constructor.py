from Sprint_3.locators import Locators
class TestConstructor:

    def test_constructor_souce(self, driver):
        driver.find_element(*Locators.button_sauces).click()
        title_sauce = driver.find_element(*Locators.title_sauce)
        example_sauce = driver.find_element(*Locators.example_sauce_spicy_x)
        assert title_sauce.text == 'Соусы' and example_sauce.text == 'Соус Spicy-X', 'Название раздела называется "Соусы" и  Соус Spicy-X отображается'

    def test_constructor_filling(self, driver):
        driver.find_element(*Locators.button_fillings).click()
        title_fillings = driver.find_element(*Locators.title_fillings)
        example_fillings = driver.find_element(*Locators.example_fillings_steak)
        assert title_fillings.text == 'Начинки' and example_fillings.text == 'Говяжий метеорит (отбивная)', 'Название раздела называется "Начинки" и  Говяжий метеорит (отбивная) отображается'

    def test_constructor_breads_tab(self, driver):
        driver.find_element(*Locators.button_fillings).click()
        driver.find_element(*Locators.button_breads).click()
        title_breads = driver.find_element(*Locators.title_breads)
        example_breads = driver.find_element(*Locators.example_breads_r2_d3)
        assert title_breads.text == 'Булки' and example_breads.text == 'Флюоресцентная булка R2-D3', 'Название раздела называется "Булки" и  Флюоресцентная булка R2-D3 отображается'
