from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

from helpers import amount

Window.size = (400, 700)


class app(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.amount = Builder.load_string(amount)
        payto = MDLabel(text="You are paying", halign="center", font_style="H4",
                        pos_hint={"center_x": 0.5, "center_y": 0.9})
        payto_user = MDLabel(text="Sardarbucks", halign="center", font_style="H4",
                        pos_hint={"center_x": 0.5, "center_y": 0.84}, bold=True)
        userbal = MDLabel(text="Your reward points: 500", halign="center", font_style="Subtitle2",
                        pos_hint={"center_x": 0.5, "center_y": 0.6}, theme_text_color="Secondary")
        button = MDRaisedButton(text="        Pay        ", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                on_release=self.show_data)
        screen.add_widget(payto)
        screen.add_widget(payto_user)
        screen.add_widget(userbal)
        screen.add_widget(self.amount)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        print("Amount is:", self.amount.text)


app().run()
