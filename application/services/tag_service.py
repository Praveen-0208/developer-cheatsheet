from application.models.Tag import Tag
from application.app import db
from flask import jsonify
import traceback

class TagService:
	def create_tag(self, params):
		try:
			tag_object = Tag(tag_name = params["tag_name"])
			db.session.add(tag_object)
			db.session.commit()
			return {"Message": "Tag created successfully"}, 200
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500
	
	def get_all_tags(self):
		try:
			tags = Tag.query.filter_by(is_deleted= False).all()
			response = [{"id": tag.id, "tag_name": tag.tag_name, "is_deleted": tag.is_deleted, "created_date": tag.created_date, "updated_date": tag.updated_date } for tag in tags]
			return jsonify(response), 200
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500

	def update_tag(self, id, params):
		try:
			tag = Tag.query.filter_by(id=id, is_deleted=False).first()
			setattr(tag, "tag_name", params["tag_name"])
			db.session.commit()
			return {"Message": "Tag updated successfully"}, 200
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500

	def delete_tag(self, id):
		try:
			tag = Tag.query.filter_by(id=id, is_deleted=False).first()
			setattr(tag, "is_deleted", True)
			db.session.commit()
			return {"Message": "Tag deleted successfully"}, 200
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500