from selenium.webdriver.common.by import By


class TestLocators:
    """Локаторы используют путь XPATH до элементов"""

    LINK_TO_PROFILE = By.XPATH, ".//*[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"
    ANCHOR_FAILD_PASSWORD = By.XPATH, (".//*[@class='input__error text_type_main-default' and text()='Некорректный "
                                       "пароль']")
    BUTTON_INNER_MAIN = By.XPATH, (".//*[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                   "button_button_size_large__G21Vg' and text()='Войти в аккаунт']")
    LINK_A_REGISTRATION_ON_PROFILE = By.XPATH, ".//*[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']"
    LINK_INNER_ON_REGITRATION_PAGE = By.XPATH, ".//*[@class='Auth_link__1fOlj' and text()='Войти']"
    INPUT_EMAIL_INNER_FORM = By.XPATH, (".//*[@class='input__placeholder text noselect text_type_main-default' and "
                                        "text()='Email']/parent::div/input")
    INPUT_PASSWORD_INNER_FORM = By.XPATH, (".//*[@class='input__placeholder text noselect text_type_main-default' and "
                                           "text()='Пароль']/parent::div/input")
    BUTTON_INNER = By.XPATH, (".//*[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                              "button_button_size_medium__3zxIa' and text()='Войти']")
    BUTTON_CONSTRUCTOR = By.XPATH, ".//*[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"
    LOGO = By.XPATH, ".//*[@class='AppHeader_header__logo__2D0X2']"
    BUTTON_QUIT = By.XPATH, (".//*[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and "
                             "text()='Выход']")
    BUTTON_SAUSE = By.XPATH, ".//*[@class='text text_type_main-default' and text()='Соусы']"
    BUTTON_BREAD = By.XPATH, ".//*[@class='text text_type_main-default' and text()='Булки']"
    BUTTON_FILLING = By.XPATH, ".//*[@class='text text_type_main-default' and text()='Начинки']"
    ANCHOR_CONSTRUCTOR_SELECTED_BUTTON = By.XPATH, (".//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 "
                                                    "pr-10 pb-4 pl-10 noselect']")
    INPUT_NAME_ON_REGISTRATION_FORM = By.XPATH, (".//*[@class='input__placeholder text noselect "
                                                 "text_type_main-default' and text()='Имя']/parent::div/input")
    INPUT_MAIL_ON_REGISTRATION_FORM = By.XPATH, (".//*[@class='input__placeholder text noselect "
                                                 "text_type_main-default' and text()='Email']/parent::div/input")
    INPUT_PASSWORD_ON_REGISTRATION_FORM = By.XPATH, (".//*[@class='input__placeholder text noselect "
                                                     "text_type_main-default' and text()='Пароль']/parent::div/input")
    BUTTON_REGISTRATION = By.XPATH, (".//*[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                     "button_button_size_medium__3zxIa' and text()='Зарегистрироваться']")
    LINK_FORGOT_PASSWORD = By.XPATH, ".//*[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"
    INPUT_EMAIL_FORGOT_FORM = By.XPATH, (".//*[@class='input__placeholder text noselect text_type_main-default' and "
                                         "text()='Email']/parent::div/input")
    BUTTON_RECOVER = By.XPATH, (".//*[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                "button_button_size_medium__3zxIa' and text()='Восстановить']")






