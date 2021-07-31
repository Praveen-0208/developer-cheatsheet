from enum import unique
from application.app import app, db
import datetime

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tag_name = db.Column(db.String(50), nullable=False, unique=True )
	is_deleted = db.Column(db.Boolean, default = False)
	created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
	updated_date = db.Column(db.DateTime, default = datetime.datetime.utcnow())

db.create_all()
db.init_app(app)