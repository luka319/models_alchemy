
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import *

SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = True


db = SQLAlchemy(app)
#db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username

