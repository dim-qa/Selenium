import data
from locators_for_tests import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestSwitch:
    """Класс содержит методы для теста переходов по страницам,
    локаторы сохранены в locators_for_tests.py
    переменные начинающиеся ANCHOR для ожиданий, BUTTON кнопки,
    LINK хранит ссылку, INPUT путь до полей ввода,
    используется явное ожидание,
    для авторизации используется одна почта и один пароль"""
    # Переход в личный кабинет
    # Проверь, переход по клику на «Личный кабинет»
    def test_click_to_profile(self, driver):
        """Авторизация и с главной страницы вход в личный кабинет"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.BUTTON_INNER_MAIN).click()
        driver.find_element(*TestLocators.INPUT_EMAIL_INNER_FORM).send_keys(data.test_mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_INNER_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_INNER).click()
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_matches(data.link_profile_page))
        assert driver.current_url == data.link_profile_page

    # Переход из личного кабинета в конструктор
    # Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers
    def test_switch_from_profile_to_constructor(self, driver):
        """Авторизация и вход в личный кабинет
         и переход по кнопке Конструктор на главную страницу"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_matches(data.link_inner_page))
        driver.find_element(*TestLocators.INPUT_EMAIL_INNER_FORM).send_keys(data.test_mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_INNER_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_INNER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_of_site))
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_of_site))
        assert driver.current_url == data.link_of_site

    # Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers
    def test_switch_from_profile_to_logo(self, driver):
        """Авторизация и вход в личный кабинет
        и переход по логотипу на главную страницу"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_inner_page))
        driver.find_element(*TestLocators.INPUT_EMAIL_INNER_FORM).send_keys(data.test_mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD_INNER_FORM).send_keys(data.password)
        driver.find_element(*TestLocators.BUTTON_INNER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_of_site))
        driver.find_element(*TestLocators.LINK_TO_PROFILE).click()
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(data.link_of_site))
        assert driver.current_url == data.link_of_site

    # Раздел «Конструктор»
    # Проверь, что работают переходы к разделам:

    # «Булки»
    def test_constructor_switch_to_bread(self, driver):
        """Выбор кнопки Соусы
        и переход на кнопку Булки"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.BUTTON_SAUSE).click()
        driver.find_element(*TestLocators.BUTTON_BREAD).click()
        current = driver.find_element(*TestLocators.ANCHOR_CONSTRUCTOR_SELECTED_BUTTON).get_attribute('class')
        lst = current.replace('_', ' ').split()
        assert 'current' in lst

        # «Соусы»

    def test_constructor_switch_to_sauce(self, driver):
        """Выбор кнопки Начинки
        и переход на кнопку Соусы"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.BUTTON_FILLING).click()
        driver.find_element(*TestLocators.BUTTON_SAUSE).click()
        current = driver.find_element(*TestLocators.ANCHOR_CONSTRUCTOR_SELECTED_BUTTON).get_attribute('class')
        lst = current.replace('_', ' ').split()
        assert 'current' in lst

        # «Начинки»

    def test_construktor_switch_to_topping(self, driver):
        """Выбор кнопки Соусы и
        переход на кнопку Начинки"""
        driver.get(data.link_of_site)
        driver.find_element(*TestLocators.BUTTON_SAUSE).click()
        driver.find_element(*TestLocators.BUTTON_FILLING).click()
        current = driver.find_element(*TestLocators.ANCHOR_CONSTRUCTOR_SELECTED_BUTTON).get_attribute('class')
        lst = current.replace('_', ' ').split()
        assert 'current' in lst
