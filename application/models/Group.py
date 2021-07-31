from application.app import app, db
import datetime

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), unique=True, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow())
    updated_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow())



db.create_all()
db.init_app(app)