from application.models.User import User
from application.app import db
import traceback

class UserService:
	def create_user(self, params):
		try:
			user_object = User(first_name=params["first_name"], last_name=params["last_name"],
						email=params["email"], password=params["password"], salt=params["salt"])
			db.session.add(user_object)
			db.session.commit()
			return {"Message": "User created"}, 200
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500

	def get_user_by_id(self, id):
		try:
			user = User.query.get(id)
			response = {
				"first_name": user.first_name,
				"email": user.email,
				"last_name": user.last_name
			}
			return response, 200
		except AttributeError as ex:
			return {"Message": "User not found", "exception": traceback.format_exc()}, 404
		except Exception as ex:
			print(ex)
			return {"Message": "Something went wrong","exception": traceback.format_exc()}, 500