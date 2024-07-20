import data
from locators_for_tests import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAutorization:
    """Класс содержит методы для теста авторизации,
    локаторы сохранены в locators_for_tests.py
    переменные начинающиеся ANCHOR для ожиданий, BUTTON кнопки,
    LINK хранит ссылку, INPUT путь до полей ввода,
    используется явное ожидание,
    при автризации использует одна почта и один пароль"""

    # Вход
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_inner_button_on_main(self, driver):
        """Вход через кнопку Войти в аккаунт на
        главной странице"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.BUTTON_INNER_MAIN).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_INNER_FORM).send_keys(data.test_mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_INNER_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_INNER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_of_site))
        assert driver.current_url == data.link_of_site

        # вход через кнопку «Личный кабинет»

    def test_inner_button_profile(self, driver):
        """Вход через кнопку Личный кабинет
        на главной странице"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_INNER_FORM).send_keys(data.test_mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_INNER_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_INNER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_of_site))
        assert driver.current_url == data.link_of_site

    # вход через кнопку в форме регистрации

    def test_inner_button_registration(self, driver):
        """Вход через ссылку "Войти" на странице регистрации"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        driver.find_element(*TestLocators.LINK_A_REGISTRATION_ON_PROFILE).click()
        driver.find_element(*TestLocators.LINK_INNER_ON_REGITRATION_PAGE).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_INNER_FORM).send_keys(data.test_mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_INNER_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_INNER).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(data.link_of_site))
        assert driver.current_url == data.link_of_site

    # вход через кнопку в форме восстановления пароля

    def test_inner_button_recovery_form(self, driver):
        """Вход через ссылку Войти на странице восстановления пароля"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        driver.find_element(*TestLocators.LINK_FORGOT_PASSWORD).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_FORGOT_FORM).send_keys(data.test_mail)
        driver.find_element(*TestLocators.BUTTON_RECOVER).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(data.link_code_forgot_password))
        assert driver.current_url == data.link_code_forgot_password

    # Выход из аккаунта
    # Проверь выход по кнопке «Выйти» в личном кабинете
    def test_quit_from_profile(self, driver):
        """Выход в личном кабинете"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_inner_page))
        driver.find_element(*TestLocators.INPUT_EMAIL_INNER_FORM).send_keys(data.test_mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_INNER_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_INNER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_of_site))
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_profile_page))
        driver.find_element(*TestLocators.BUTTON_QUIT).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_inner_page))
        assert driver.current_url == data.link_inner_page
