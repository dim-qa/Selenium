https://stellarburgers.nomoreparties.site/
Тестирование UI регистрации, авторизации, переход по блокам


    # Регистрация 
        # Успешная регистрация
        def test_registration_input_name_mail_password(self, driver):
    
        # Неуспешная регистрация без имени
        def test_registration_without_name(self, driver):
    
        # Неуспешная регистрация с паролем менее 6 символов
        def test_registration_faild_password(self, driver):


    # Вход
        # Вход по кнопке «Войти в аккаунт» на главной
        def test_inner_button_on_main(self, driver):
     
    
        # вход через кнопку «Личный кабинет»
        def test_inner_button_profile(self, driver):
    
        # вход через кнопку в форме регистрации
        def test_inner_button_registration(self, driver):
            
        # вход через кнопку в форме восстановления пароля
        def test_inner_button_recovery_form(self, driver):
        

    # Переход в личный кабинет
        # Проверь переход по клику на «Личный кабинет»
        def test_click_to_profile(self, driver):
            
        # Переход из личного кабинета в конструктор
        # Проверь переход по клику на «Конструктор»
        def test_switch_from_profile_to_constructor(self, driver):
            
        # Проверь переход по клику на логотип Stellar Burgers
        def test_switch_from_profile_to_logo(self, driver):
        

    # Выход из аккаунта
        # Проверь выход по кнопке «Выйти» в личном кабинете
        def test_quit_from_profile(self, driver):
        

    # Раздел «Конструктор»
        # Проверь, что работают переходы к разделам:    
            # «Булки»
            def test_constructor_switch_to_bread(self, driver):
               
            # «Соусы»
            def test_constructor_switch_to_sauce(self, driver):
        
            # «Начинки»
            def test_construktor_switch_to_topping(self, driver):
       