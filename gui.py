from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
import datetime

KV = '''
ScreenManager:
    WelcomeScreen:
    LoginScreen:
    RegScreen:
    SuccessLoginScreen:
    SuccessRegScreen:
    MainMenuScreen:

<WelcomeScreen>:
    name: 'welcome'
    MDLabel:
        text: 'Price Control'
        halign: 'left'
        pos_hint: {'center_y': 0.95}
        font_style: 'H4'
    MDLabel:
        text: 'Добро пожаловать!'
        halign: 'center'
        pos_hint: {'center_y': 0.6}
        font_style: 'H5'
    MDRectangleFlatButton:
        text: 'Войти'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        on_release: app.root.current = 'login'
        md_bg_color: app.theme_cls.primary_color
        text_color: 1, 1, 1, 1
    MDRectangleFlatButton:
        text: 'У меня пока нет аккаунта'
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        on_release: app.root.current = 'register'
        md_bg_color: app.theme_cls.accent_color
        text_color: 1, 1, 1, 1

<LoginScreen>:
    name: 'login'
    MDLabel:
        text: 'Price Control'
        pos_hint: {'center_x': 0.55, 'center_y': 0.95}
        halign: 'left'
        font_style: 'H6'
    MDTextField:
        id: login_field
        hint_text: "Логин"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
        line_color_normal: app.theme_cls.primary_light
        line_color_focus: app.theme_cls.primary_dark
    MDTextField:
        id: password_field
        hint_text: "Пароль"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        password: True
        line_color_normal: app.theme_cls.primary_light
        line_color_focus: app.theme_cls.primary_dark
    MDRectangleFlatButton:
        text: 'Войти'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.check_login()
        md_bg_color: app.theme_cls.primary_color
        text_color: 1, 1, 1, 1
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.current = 'welcome'
        md_bg_color: app.theme_cls.accent_light
        text_color: 1, 1, 1, 1

<RegScreen>:
    name: 'register'
    MDLabel:
        text: 'Price Control'
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        halign: 'left'
        font_style: 'H6'
    MDTextField:
        id: name_field
        hint_text: "Имя"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint_x: None
        width: 300
        line_color_normal: app.theme_cls.primary_light
        line_color_focus: app.theme_cls.primary_dark
    MDTextField:
        id: phone_field
        hint_text: "Телефон"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
        line_color_normal: app.theme_cls.primary_light
        line_color_focus: app.theme_cls.primary_dark
    MDTextField:
        id: email_field
        hint_text: "Логин (email)"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
        line_color_normal: app.theme_cls.primary_light
        line_color_focus: app.theme_cls.primary_dark
    MDRectangleFlatButton:
        text: 'Создать аккаунт'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: app.check_register()
        md_bg_color: app.theme_cls.accent_color
        text_color: 1, 1, 1, 1
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.current = 'welcome'
        md_bg_color: app.theme_cls.accent_light
        text_color: 1, 1, 1, 1

<SuccessLoginScreen>:
    name: 'success_login'
    MDLabel:
        text: 'Price Control'
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        halign: 'left'
        font_style: 'H6'
    MDLabel:
        text: 'Вы успешно вошли в систему!'
        halign: 'center'
        pos_hint: {'center_y': 0.5}
        font_style: 'H5'

<SuccessRegScreen>:
    name: 'success_register'
    MDLabel:
        text: 'Price Control'
        pos_hint: {'center_x': 0.1, 'center_y': 0.95}
        halign: 'left'
        font_style: 'H6'
    MDLabel:
        id: label
        halign: 'center'
        pos_hint: {'center_y': 0.5}
        font_style: 'H5'
    MDRectangleFlatButton:
        text: 'Войти'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.root.current = 'login'
        md_bg_color: app.theme_cls.primary_color
        text_color: 1, 1, 1, 1

<MainMenuScreen>:
    name: 'main_menu'
    FloatLayout:
        MDTopAppBar:
            title: 'Price Control'
            pos_hint: {'top': 1}
            size_hint_y: None
            height: '56dp'  

        MDLabel:
            id: greeting
            text: ''
            halign: 'left'
            size_hint_y: None
            height: '48dp'
            pos_hint: {'x': 0, 'y': 0.8}
            padding_x: 10

        MDFillRoundFlatButton:
            text: 'Загрузить изображение'
            icon: 'camera'
            size_hint: None, None
            size: '200dp', '48dp'
            pos_hint: {'center_x': 0.5, 'y': 0.5}

        MDFillRoundFlatButton:
            text: 'Поиск'
            icon: 'magnify'
            size_hint: None, None
            size: '200dp', '48dp'
            pos_hint: {'center_x': 0.5, 'y': 0.4}


'''

class WelcomeScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass

class RegScreen(MDScreen):
    pass

class SuccessLoginScreen(MDScreen):
    pass

class SuccessRegScreen(MDScreen):
    pass

class MainMenuScreen(MDScreen):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Amber'
        return Builder.load_string(KV)

    def on_start(self):
        self.set_greeting()

    def set_greeting(self):
        current_time = datetime.datetime.now()
        if 5 <= current_time.hour < 12:
            greeting = 'Доброе утро, '
        elif 12 <= current_time.hour < 18:
            greeting = 'Добрый день, '
        else:
            greeting = 'Добрый вечер, '
        user_name = 'Администратор'
        self.root.get_screen('main_menu').ids.greeting.text = greeting + user_name

    def load_image(self):
        # Здесь должен быть вызов функции для загрузки изображения из галереи или камеры
        print("Загрузка изображения...")

    def search_item(self):
        print("Поиск завершен успешно!")

    def check_login(self):
        login = self.root.get_screen('login').ids.login_field
        password = self.root.get_screen('login').ids.password_field
        if login.text == 'admin' and password.text == 'admin':
            self.root.current = 'main_menu'
        else:
            if login.text.strip() == '':
                login.line_color_normal = (1, 0, 0, 1)
            if password.text.strip() == '':
                password.line_color_normal = (1, 0, 0, 1)

    def check_register(self):
        name = self.root.get_screen('register').ids.name_field
        phone = self.root.get_screen('register').ids.phone_field
        email = self.root.get_screen('register').ids.email_field
        if name.text.strip() == '' or phone.text.strip() == '' or email.text.strip() == '':
            if name.text.strip() == '':
                name.line_color_normal = (1, 0, 0, 1)
            if phone.text.strip() == '':
                phone.line_color_normal = (1, 0, 0, 1)
            if email.text.strip() == '':
                email.line_color_normal = (1, 0, 0, 1)
            return
        user_name = name.text.strip()
        self.root.get_screen('success_register').ids.label.text = f'Поздравляем, {user_name}! Вы успешно зарегистрированы.'
        self.root.current = 'success_register'

if __name__ == '__main__':
    MyApp().run()
