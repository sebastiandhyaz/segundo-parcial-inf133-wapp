    from flask_sqlalchemy import SQLAlchemy
    from flask_login import UserMixin
    from werkzeug.security import generate_password_hash, check_password_hash
    from app import db

    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        username = db.Column(db.String(150), unique=True, nullable=False)
        password = db.Column(db.String(150), nullable=False)
        role = db.Column(db.String(50), nullable=False)

        def set_password(self, password):
            self.password = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password, password)

    class Patient(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String(150), nullable=False)
        lastname = db.Column(db.String(150), nullable=False)
        ci = db.Column(db.String(20), unique=True, nullable=False)
        birth_date = db.Column(db.String(50), nullable=False)