from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app import views, models

# Instantiate our app and load configuration
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


