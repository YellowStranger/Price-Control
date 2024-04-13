from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from app_net import Socket
from plyer import filechooser, camera
import asyncio
import datetime

sock = Socket()

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
    BoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            size_hint_y: None
            height: '200dp'
            MDIconButton:
                icon: 'arrow-left'
                user_font_size: '48sp'
                pos_hint: {'center_x': 0.1, 'center_y': 0.5}
                on_release: app.close_app()
            MDLabel:
                text: 'Price Control'
                halign: 'center'
                valign: 'middle'
                font_style: 'H2'
                size_hint_y: None
                height: self.texture_size[1]
        Image:
            source: 'welcome_background.png'
            allow_stretch: True
            keep_ratio: False
        MDBoxLayout:
            adaptive_height: True
            padding: dp(24)
            spacing: dp(16)
            pos_hint: {'center_x': 0.5, 'bottom': 1}

            MDRaisedButton:
                text: 'Войти'
                on_release: app.root.current = 'login'
                md_bg_color: app.theme_cls.primary_color
                text_color: 1, 1, 1, 1

            MDRaisedButton:
                text: 'Регистрация'
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
    MDTextField:
        id: password_field
        hint_text: "Пароль"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}  # Обнови значение 'center_y', чтобы корректно расположить поля
        size_hint_x: None
        width: 300
        password: True
        line_color_normal: app.theme_cls.primary_light
        line_color_focus: app.theme_cls.primary_dark
    MDRectangleFlatButton:
        text: 'Создать аккаунт'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.check_register()
        md_bg_color: app.theme_cls.accent_color
        text_color: 1, 1, 1, 1
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
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
            elevation: 10

        MDLabel:
            id: greeting
            text: ''
            halign: 'left'
            pos_hint: {'center_x': 0.55, 'center_y': 0.8}
            font_style: 'Subtitle1'

        MDLabel:
            text: 'Выберите источник фото:'
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            font_style: 'Subtitle1'

        MDFillRoundFlatButton:
            text: 'Сделать фото'
            icon: 'camera'
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            on_release: app.take_photo()
            md_bg_color: app.theme_cls.primary_color
            text_color: 1, 1, 1, 1

        MDFillRoundFlatButton:
            text: 'Выбрать из галереи'
            icon: 'image-multiple'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.load_image()
            md_bg_color: app.theme_cls.accent_color
            text_color: 1, 1, 1, 1
               
        MDIconButton:
            id: menu_button
            icon: 'menu'
            user_font_size: '24sp'
            pos_hint: {'center_x': 0.95, 'center_y': 0.945}
            on_release: app.open_menu(self)


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

class PriceControl(MDApp):
    dialog = None
    menu = None
    
    async def app_run(self):
        await self.async_run(async_lib='asyncio')
    def sock_close(self, *kwargs):
        asyncio.create_task(sock.close())

    def build(self):
        asyncio.create_task(sock.start())
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Amber'
        Window.bind(on_request_close=self.sock_close)
        return Builder.load_string(KV)

    def create_menu(self, caller_widget):
        menu_items = [
            {"text": "Главная"},
            {"text": "Категории"},
            {"text": "Мои запросы"},
            {"text": "Магазины"},
            {"text": "Связаться с нами"}
        ]
        self.menu = MDDropdownMenu(
            caller=caller_widget,
            items=menu_items,
            width_mult=4,
        )

    def open_menu(self, caller_widget):
        if not self.menu:
            self.create_menu(caller_widget)
        self.menu.open()


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
        self.root.get_screen('main_menu').ids.greeting.text = greeting + user_name + ' !'

    def dialog_choice(self, title, camera_text, gallery_text):
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                type="confirmation",
                items=[
                    MDFlatButton(
                        text=camera_text,
                        on_release=lambda _: self.resolve_choice("camera")
                    ),
                    MDFlatButton(
                        text=gallery_text,
                        on_release=lambda _: self.resolve_choice("gallery")
                    ),
                ],
                buttons=[
                    MDFlatButton(
                        text="Отмена",
                        on_release=lambda _: self.dialog.dismiss()
                    )
                ]
            )
        self.dialog.open()

    def resolve_choice(self, choice):
        self.dialog.dismiss()
        if choice == "camera":
            self.take_photo()
        elif choice == "gallery":
            filechooser.open_file(on_selection=self.selected_image, filters=["*.png", "*.jpg", "*.jpeg"])

    def load_image(self):
        self.dialog_choice("Выберите действие", "Использовать камеру", "Выбрать из галереи")

    def photo_taken(self, result):
        if result:
            print(f"Фотография сохранена: {result}")
        else:
            print("Не удалось сделать фото.")

    def take_photo(self):
        path_to_save_image = MDApp.get_running_app().user_data_dir + '/photo.jpg'
        camera.take_picture(filename=path_to_save_image, on_complete=self.photo_taken)

    def selected_image(self, selection):
        if selection:
            self.root.get_screen('main_menu').ids.photo.source = selection[0]

    def search_item(self):
        print("Поиск завершен успешно!")

    def check_login(self):
        self.login = self.root.get_screen('login').ids.login_field
        self.password = self.root.get_screen('login').ids.password_field
        self.sock_start = asyncio.create_task(sock.login(self.login.text, self.password.text))
        # отслеживание завершения авторизации 
        self.schedule_event = Clock.schedule_interval(self.check_handshake_complete, 0.3)

    def check_register(self):
        self.bname = self.root.get_screen('register').ids.name_field
        self.phone = self.root.get_screen('register').ids.phone_field
        self.email = self.root.get_screen('register').ids.email_field
        self.password = self.root.get_screen('register').ids.password_field
        
        self.sock_start = asyncio.create_task(sock.register(self.email.text, self.password.text, phone=self.phone.text))
        self.schedule_event = Clock.schedule_interval(self.check_handshake_complete, 0.3)

        user_name = self.bname.text.strip()
        self.root.get_screen('success_register').ids.label.text = f'Поздравляем, {user_name}! Вы успешно зарегистрированы.'
        self.root.current = 'success_register'
    
    def check_handshake_complete(self, *kwargs):
        try:
        
            if sock.event == "login":
                
                # авторизация прошла успешно
                if sock.correct:
                    #self.username = self.sock_start.result()
                    self.root.current = 'main_menu'
                    self.schedule_event.cancel()
                    sock.correct = False
                else :
                    self.schedule_event.cancel()
                    if self.login.text.strip() == '':
                        self.login.line_color_normal = (1, 0, 0, 1)
                    if self.password.text.strip() == '':
                        self.password.line_color_normal = (1, 0, 0, 1)
                

            elif sock.event == 'register':
                if sock.correct:
                    user_name = self.bname.text.strip()
                    self.root.get_screen('success_register')
                    self.root.current = 'success_register'
                    sock.correct = False
                    self.schedule_event.cancel()

                else:
                    self.schedule_event.cancel()
                    if self.bname.text.strip() == '' or self.phone.text.strip() == '' or self.email.text.strip() == '':
                        if self.bname.text.strip() == '':
                            self.bname.line_color_normal = (1, 0, 0, 1)
                        if self.phone.text.strip() == '':
                            self.phone.line_color_normal = (1, 0, 0, 1)
                        if self.email.text.strip() == '':
                            self.email.line_color_normal = (1, 0, 0, 1)
                        self.schedule_event.cancel()
        except AttributeError:
            pass

if __name__ == '__main__':
    asyncio.run(PriceControl().app_run())
