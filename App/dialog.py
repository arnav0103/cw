from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.core.window import Window
import json

Window.size = (400, 700)


from helpers import amount

class my_app(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.amount = Builder.load_string(amount)
        a_file = open("transaction.json", "r")
        json_objects = json.load(a_file)
        a_file.close()
        payto = MDLabel(text="You are paying", halign="center", font_style="H4",
                        pos_hint={"center_x": 0.5, "center_y": 0.9})
        payto_user = MDLabel(text=json_objects["receiver"], halign="center", font_style="H4",
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
            # a_file = open("transaction.json", "r")
            # json_objects = json.load(a_file)
            # a_file.close()
            # json_objects['amount'] = self.amount.text
            # a_file = open("transaction.json", "w")
            # json.dump(json_objects, a_file)
            # a_file.close()
            # with app.app_context():
            #     connect_node()
            #     add_transaction()
            #     replace_chain()
            a_file = open("transaction.json", "r")
            json_objects = json.load(a_file)
            amount = int(self.amount.text)
            if amount > 500:
                dialog = MDDialog(title = "ERROR",text=f'There was an error while paying {json_objects["receiver"]},', buttons=[
                    MDFlatButton(
                        text="CLOSE", text_color=self.theme_cls.primary_color
                    ),
                ],)
            else:
                dialog = MDDialog(title = "Success",text=f'Successfuly paid {json_objects["receiver"]}' , buttons=[
                    MDFlatButton(
                        text="CLOSE", text_color=self.theme_cls.primary_color
                    ),
                ],)
                

            dialog.open()
my_app().run()