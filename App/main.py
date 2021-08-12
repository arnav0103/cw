from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import Screen
from kivy.core.window import Window

Window.size = (400, 700)


from helpers import username_text, pass_text


class app(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.username = Builder.load_string(username_text)
        self.password = Builder.load_string(pass_text)
        button = MDRaisedButton(text="Submit", pos_hint={"center_x": 0.5, "center_y": 0.4}, on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            dialog = MDDialog(text="Please don't leave input empty")
            dialog.open()
        elif self.password.text is "":
            dialog = MDDialog(text="Please don't leave input empty")
            dialog.open()
        else:
            print("Username:", self.username.text)
            print("Password:", self.password.text)


app().run()
