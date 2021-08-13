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
from flask_pymongo import PyMongo
from pymongo import MongoClient
from Tool import app,mongo


@app.route('/')
def index():
    user_collection = mongo.db.users
    user_collection.insert({'name': 'Tijil', 'amount' : '500'})
    user_collection.insert({'name': 'Arnav', 'amount' : '0'})
    return "<h1> USER ADDED </h1>"

if __name__ == '__main__':
    app.run(debug=True)
