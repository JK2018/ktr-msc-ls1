from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aRandomSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data2.db'

db2 = SQLAlchemy(app)

from routes import *


if __name__ == '__main__':
    app.run(debug=True)
