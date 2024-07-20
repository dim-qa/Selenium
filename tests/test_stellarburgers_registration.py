import data
from locators_for_tests import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:
    """Класс содержит методы для теста регистрации,
    локаторы сохранены в locators_for_tests.py
    переменные начинающиеся ANCHOR для ожиданий, BUTTON кнопки,
    LINK хранит ссылку, INPUT путь до полей ввода,
    используется явное ожидание,
    при регистрации используется метод randomint
    и конкатенация со строкой для уникальных данных"""

    # Регистрация
    def test_registration_input_name_mail_password(self, driver):
        """успешная регистрация
        валидные имя почта пароль"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        driver.find_element(*TestLocators.LINK_A_REGISTRATION_ON_PROFILE).click()
        driver.find_element(*TestLocators.INPUT_NAME_ON_REGISTRATION_FORM).send_keys(data.name)
        driver.find_element(*TestLocators.INPUT_MAIL_ON_REGISTRATION_FORM).send_keys(data.mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_ON_REGISTRATION_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_inner_page))
        assert driver.current_url == data.link_inner_page

    def test_registration_without_name(self, driver):
        """неуспешная регистрация без имени"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        driver.find_element(*TestLocators.LINK_A_REGISTRATION_ON_PROFILE).click()
        driver.find_element(*TestLocators.INPUT_MAIL_ON_REGISTRATION_FORM).send_keys(data.mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_ON_REGISTRATION_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        assert driver.current_url == data.link_register_page

    def test_registration_faild_password(self, driver):
        """неуспешная регистрация при невалидном пароле"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        driver.find_element(*TestLocators.LINK_A_REGISTRATION_ON_PROFILE).click()
        driver.find_element(*TestLocators.INPUT_NAME_ON_REGISTRATION_FORM).send_keys(data.name)
        driver.find_element(*TestLocators.INPUT_MAIL_ON_REGISTRATION_FORM).send_keys(data.mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_ON_REGISTRATION_FORM).send_keys('3')
        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*TestLocators.ANCHOR_FAILD_PASSWORD).text == 'Некорректный пароль'




