from application.models.Entry import Entry
from application.app import db
from flask import jsonify
import traceback

class EntryService:
	def create_entry(self, params):
		try:
			pass
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500
	
	def get_all_entries(self, group_id=None, tag_id=None):
		try:
			if((group_id is not None) and (tag_id is not None)):
				entries = Entry.query.order_by(Entry.created_date).filter_by(group_id=group_id, tag_id=tag_id).all()
			elif(tag_id is not None):
				entries = Entry.query.order_by(Entry.created_date).filter_by(tag_id=tag_id).all()
			elif(group_id is not None):
				entries = Entry.query.order_by(Entry.created_date).filter_by(group_id=group_id).all()
			else:
				entries = Entry.query.order_by(Entry.created_date).all()
			return "Ok", 200
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500

	def update_entry(self, params):
		try:
			pass
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500
	
	def get_single_entry(self, id):
		try:
			# entry = Entry.query.filter_by(id=id, is_deleted=False).all()
			# response = {}
			pass
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500
	
	def delete_entry(self, id):
		try:
			pass
		except Exception as ex:
			return {"Message": "Something went wrong", "exception": traceback.format_exc()}, 500