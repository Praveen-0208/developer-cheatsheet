from application.app import db, app
import datetime

class Entry():
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
	group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable= False)
	tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable= False)
	title = db.Column(db.String(100), nullable = False)
	description = db.Column(db.String(200))
	screenShots = db.Column(db.LargeBinary)
	is_deleted = db.Column(db.Boolean, default = False)
	created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
	updated_date = db.Column(db.DateTime, default = datetime.datetime.utcnow())

db.create_all()
db.init_app(app)