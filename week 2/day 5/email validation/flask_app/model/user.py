from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self, data):
        self.id = data['id']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_user( user ):
        is_valid = True
        if not EMAIL_REGEX.match(user['email_address']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def display_user(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_validation').query_db(query)
        data = []
        for result in results:
            data.append(cls(result))
        return data
        
        

    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES (%(email_address)s, NOW(), NOW());"
        return connectToMySQL("email_validation").query_db(query, data)

    @classmethod
    def delete():
        query = "DELETE * FROM emails WHERE id = emails.id"