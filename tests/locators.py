from selenium.webdriver.common.by import By

NAME_INPUT = (By.NAME, 'name') # Поле для вводя Имени при регистрации
LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка для входа
FORGOT_PASSWORD_LINK = (By.XPATH, '//a[text()="Восстановить пароль"]')  # Ссылка для восстановления пароля
REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться"]')  # Ссылка для перехода к регистрации
REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')# Кнопка Зарегистрироваться 
LOGIN_ELEMENT_TEXT = (By.XPATH, ".//*[text() = 'Вход']")#Вход
EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")#Поле ввода логина
PASSWORD_INPUT = (By.XPATH, ".//input[@type='password' and @name='Пароль']")#Поле ввода пароля
REGISTRATION_ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")#Сообщение об ошибке при вводе пароля
LK_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")#Кнопка "Личный Кабинет"
LOGIN_BUTTON_MP = (By.XPATH, ".//button[text()='Войти в аккаунт']")#Кнопка "Войти в аккаунт"
ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")#Кнопка "Войти"
ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")#Кнопка "Оформить заказ"
LOGIN_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")#Ссылка логин
LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")#Кнопка "Выход"
CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")#Кнопка "Конструктор"
MAIN_LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")#Логотип
SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::*")#Вкладка "Соусы"
SAUCES_TEXT = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"#Текстовый элемент "Соусы"
BUN_TAB = (By.XPATH, ".//span[text()='Булки']/parent::*")#Вкладка "Булки"
BUN_TEXT = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"#Текстовый элемент "Булки"
FILLING_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::*")#Вкладка "Начинки"
FILLING_TEXT = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"#Текстовый элемент "Начинки"
