# FISIteka/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

# Configuración de la aplicación desde un archivo config.py
app.config.from_object('config.Config')

# Configuración de la base de datos
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configuración de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'views.auth_views.login'

from app.views import test, auth_views, resource_views, user_views