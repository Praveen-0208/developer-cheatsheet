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


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), unique=True, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow())
    updated_date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow())
# Sample for One-many and Many-Many relationship
# class WorkItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(120))

#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     shared_with = db.relationship('User', secondary=shared_with, lazy='subquery', backref=db.backref('user', lazy=True))

# shared_with = db.Table('shared_with',
#     db.Column('work_item_id', db.Integer, db.ForeignKey('work_item.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

# Using the above sample write the DB models here


db.create_all()
db.init_app(app)


def create_user(params):
    try:
        user_object = User(first_name=params["first_name"], last_name=params["last_name"],
                    email=params["email"], password=params["password"], salt=params["salt"])
        db.session.add(user_object)
        db.session.commit()
        return {"Status": "200", "Message": "User created"}
    except Exception as ex:
        return {"Status":"500", "Message": str(ex)}

def get_user_by_id(id):
    try:
        pass
    except Exception as ex:
        return {"Status": "500", "Message": str(ex)}