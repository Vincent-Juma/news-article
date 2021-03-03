import os

class Config:
  '''
  general configuration parent class
  '''

  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')

  pass

class ProdConfig(Config):
  '''
  production configuration child class
  Args:
    Config: The Parent configuration class with general configuration settings
  '''

  pass

class DevConfig(Config):
  '''
  development configuration child class
  Args:
    Config: The Parent configuration class with general configuration settings
  '''

  DEBUG = True

config_options = {
  'development': DevConfig,
  'production': ProdConfig
}
# # from flask import Flask
# # from .config import DevConfig

# # # Initializing application
# # app = Flask(__name__,instance_relative_config = True)

# # # Setting up configuration
# # app.config.from_object(DevConfig)
# # app.config.from_pyfile('config.py')

# # from app import views
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager

# app = Flask(__name__)
# NEWS_API_KEY = '3c82ea4131dd41b0b777eee004edca9c'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

# from flaskblog import routes