
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt



from datetime import timedelta

app = Flask(__name__)


app.config["SECRET_KEY"] = 'b668cbc68d29fd2b7f5976c54c39f6ec'
app.config['WTF_CSRF_SECRET_KEY'] = 'fe9d487ba2c9a1f13a5d72fa0d76d3fb'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///team19.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=30)




db = SQLAlchemy(app)

bcrypt = Bcrypt(app)






from islandApp import routes, models
