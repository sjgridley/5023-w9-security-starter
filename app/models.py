from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text, unique = True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)
    pets = db.relationship('Pet', backref='owner')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    owner_id = db.Column(db.ForeignKey('user.id'))
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'))
    animal = db.relationship('Animal')

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

