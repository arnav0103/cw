from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
import json
from helpers import amount
import cv2
import kivy
from pyzbar import pyzbar
import os
import threading
from kivy.uix.screenmanager import Screen,ScreenManager
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse


Window.size = (400, 700)


#######################################
class qr(MDApp):
    def read_barcodes(frame):
        barcodes = pyzbar.decode(frame)
        qr_text = ''
        cv2.rectangle(frame, (232, 181),(232+220, 181+220), (0, 255, 0), 2)
        for barcode in barcodes:
            qr_text = barcode.data.decode('utf-8')
        if qr_text:
            return frame,qr_text
        else:
            return frame,''

    def build(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame,qr_text = qr.read_barcodes(frame)
            if qr_text:

                dictionary ={
                            "sender" : "tijil",
                            "receiver" : qr_text,
                            "amount" : 10
                            }

                json_object = json.dumps(dictionary, indent = 3)
                with open("transaction.json", "w") as outfile:
                    outfile.write(json_object)

                my_app().run()
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

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
            a_file = open("transaction.json", "r")
            json_objects = json.load(a_file)
            a_file.close()
            json_objects['amount'] = self.amount.text
            a_file = open("transaction.json", "w")
            json.dump(json_objects, a_file)
            a_file.close()



qr().run()
