import os

class Config:
    SECRET_KEY = 'password'
    SQLALCHEMY_DATABASE_URI= 'mysql://root:password@db:3306/Contenedor1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False