from application.app import app, db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))
    salt = db.Column(db.String(120))
    created_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow())
    updated_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow())


db.create_all()
db.init_app(app)