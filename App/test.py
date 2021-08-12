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


new_environ = os.environ.copy()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'
def start_app():
    print("Starting Flask app...")
    app.run(port=5000, debug=False)     #specify separate port to run Flask app

class MyApp(MDApp):

    def build(self):
        hi = hello()
        return MDLabel(text=hi)

if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") != 'true':
        threading.Thread(target=start_app).start()
    MyApp().run()
