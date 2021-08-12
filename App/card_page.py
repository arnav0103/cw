from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from helpers import bottom_toolbar


class app(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        title_head = MDLabel(text="Your Cards", pos_hint={"center_x": 0.55, "center_y": 0.9}, theme_text_color='Custom', text_color=(1, 1, 1, 1),
                             font_style="H3")
        toolbar = Builder.load_string(bottom_toolbar)
        screen.add_widget(title_head)
        screen.add_widget(toolbar)
        return screen


app().run()
