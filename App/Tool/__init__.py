import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_pymongo import PyMongo
################


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://db_user:db_user_password@cluster0.jtq6d.mongodb.net/Cluster0?retryWrites=true&w=majority"
mongo = PyMongo(app)
