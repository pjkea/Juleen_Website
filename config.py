# config.py

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
