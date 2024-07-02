import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///F:/bdFlaskLite.db'  # O cualquier otra base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False