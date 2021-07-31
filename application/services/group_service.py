from flask.json import jsonify
from application.models.Group import Group
from application.app import db
import traceback

class GroupService:
	def create_group(self, params):
		try:
			group_object = Group(group_name=params["group_name"])
			db.session.add(group_object)
			db.session.commit()
			return {"Message": "Group created successfully"}, 200
		except Exception as ex:
			return {"Message": str(ex), "exception": traceback.format_exc()}, 500

	def get_all_groups(self):
		try:
			group_list = Group.query.filter_by(is_deleted=False).all()
			groups = [{"id":  group.id, "group_name": group.group_name, "isDeleted": group.is_deleted, "createdDate": group.created_date, "updatedDate": group.updated_date} for group in group_list]
			return jsonify(groups), 200
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500
	
	def update_group(self, id, params):
		try:
			group = Group.query.filter_by(id= id, is_deleted=False).first()
			if group is not None:
				# group["group_name"] = params["group_name"] 
				setattr(group, "group_name", params["group_name"])
				db.session.commit()
				return {"Message": "Group updated successully"}, 200
			return {"Message": "Group not found", "exception": traceback.format_exc()}, 404
		except Exception as ex:
			return {"Message": "Update failed", "exception": traceback.format_exc()}, 500

	def delete_group(self, id):
		try:
			group = Group.query.filter_by(id= id, is_deleted=False).first()
			if group is not None:
				# group["group_name"] = params["group_name"] 
				setattr(group, "is_deleted", True)
				db.session.commit()
				return {"Message": "Group deleted successully"}, 200
			return {"Message": "Group not found", "exception": traceback.format_exc()}, 404
		except Exception as ex:
			return {"Message": "Delete failed", "exception": traceback.format_exc()}, 500