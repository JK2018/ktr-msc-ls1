from app import db2


class User(db2.Model):
    id = db2.Column(db2.Integer, primary_key=True)
    name = db2.Column(db2.String(30), nullable=False)
    companyName = db2.Column(db2.String(30), nullable=True)
    emailAddress = db2.Column(db2.String(100), nullable=True)
    telephoneNumber = db2.Column(db2.Integer, nullable=True)
    password = db2.Column(db2.Integer, nullable=False)
    cards = db2.relationship('Card', backref='user', lazy=True)

class Card(db2.Model):
    id = db2.Column(db2.Integer, primary_key=True)
    name = db2.Column(db2.String(30), nullable=False)
    companyName = db2.Column(db2.String(30), nullable=True)
    emailAddress = db2.Column(db2.String(100), nullable=True)
    telephoneNumber = db2.Column(db2.Integer, nullable=True)
    user_id = db2.Column(db2.Integer, db2.ForeignKey('user.id'),nullable=False)