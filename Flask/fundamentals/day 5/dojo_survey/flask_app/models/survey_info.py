from ..config.mysqlconnection import connectToMySQL
from flask import flash


class Survey_info:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @staticmethod
    def validate_info(info):
        is_valid = True
        if len(info['name'])<3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(info['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid