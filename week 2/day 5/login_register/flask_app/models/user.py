from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO login_register (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        save = connectToMySQL("login_schema").query_db(query, data)
        return save

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM login_register WHERE email = %(email)s;"
        result = connectToMySQL("login_schema").query_db(query,data)
        if len(result) < 1:
            return False
        print(data)
        print(result)
        return cls(result[0])

    @staticmethod
    def login_validator(post_data):
        user_from_db = User.get_by_email({'email': post_data['email']})
        if not user_from_db:
            flash("Invalid Email.")
            return False
        if not bcrypt.check_password_hash(user_from_db.password, post_data['password']):
            flash("Invalid Password.")
            return False
        return True
    


    @staticmethod
    def validate_user( post_data ):
        is_valid = True
        if len(post_data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False

        if len(post_data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False

        if not EMAIL_REGEX.match(post_data['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(post_data['password']) < 4:
            flash("Password must be at least 4 characters.")
            is_valid = False
        elif post_data['password'] != post_data['confirm_password']:
            flash("Passwords must match!")
            is_valid = False
        return is_valid


    @classmethod
    def display(cls, data):
        query = "SELECT * FROM login_register;"
        save = connectToMySQL("login_schema").query_db(query, data)
        return save

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM login_register WHERE id = %(id)s"
        one = connectToMySQL("login_schema").query_db(query, data)
        print(one)
        user = User(one[0])
        return user