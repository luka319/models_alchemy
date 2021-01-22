#A Simple Example

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
"""
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
"""

SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = True


#db = SQLAlchemy(app)
from models import db
#from models import *
#db.init_app(app)
db.init_app()

"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username
"""

db.create_all()  # добавил, в док. не было
# ============================================

db.session.add(User(username="Flask", email="example@example.com"))
db.session.add(User(username="Django", email="dj@example.com"))
db.session.commit()

users = User.query.all()

for u in users:
    print(f"{u.username =}")
    print(f"{u =}")

