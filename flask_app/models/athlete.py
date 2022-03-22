from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash, session
from flask_app import app
import re	# the regex module
from flask_bcrypt import Bcrypt   
from flask_app.models import event, post, time     

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$')
NAME_REGEX = re.compile('^(/^[A-Za-z]+$/)')

 #CREATE model
class Athlete:
    db = 'on_track'
    def __init__(self, data): 
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.full_name = f"{data['first_name']} {data['last_name']}"
        self.coach=[]
        self.times=[]
        
        # Validate 
    @staticmethod
    def validate_submission(input):
        is_valid = True
        if len(input['first_name']) < 1:
            flash('name must enter at least 1 characters')
            is_valid = False
        if len(input['last_name']) < 1:
            flash('name must enter at least 1 characters')
            is_valid = False
        if not PASSWORD_REGEX.match(input['password']):
            flash('invalid password')
            is_valid = False
        if input['password'] != input['confirm_password']:
            flash('passwords do not match')
            is_valid = False
        if not EMAIL_REGEX.match(input['email']): 
            flash("Invalid email address!")
            is_valid = False   
        if cls.find_athlete_by_email(input):
            flash('An account already exists with this email')
            is_valid = False

    @staticmethod
    def validate_update(input):
        is_valid = True
        if len(input['first_name']) < 1:
            flash('name must enter at least 1 characters')
            is_valid = False
        if len(input['last_name']) < 1:
            flash('name must enter at least 1 characters')
            is_valid = False
        if not EMAIL_REGEX.match(input['email']): 
            flash("Invalid email address!")
            is_valid = False   
       
        return is_valid
        
    @staticmethod
    def parsed_data(data):
        parsed_data={
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'].lower().strip(),
            'password' : bcrypt.generate_password_hash(data['password']),
            'coach_id' : session['coach_id']
        }
        return parsed_data

    @classmethod
    def register_athlete(cls, data):
        ('>>>>>>>>>>i am here')
        # if not cls.validate_submission(data):
        #     return False
        data = cls.parsed_data(data)
        print(data)
        query= '''
        INSERT INTO athletes (first_name, last_name, email, password, coach_id)
        VALUES (%(first_name)s, %(last_name)s, %(email)s,%(password)s,%(coach_id)s)
        ;'''
        athlete_id = connectToMySQL(cls.db).query_db(query,data)
        print(athlete_id)
        # Removed automatic sign in upon registration for athletes 
        # because coaches will register athletes and then give them their log in information at a seperate time. 
        return athlete_id
    
    @classmethod
    def get_athletes_by_coach_id(cls, id):
        data= {'id': id}
        query = "SELECT * FROM athletes WHERE coach_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        athletes = []
        for row in results:
            athletes.append(cls(row))
        return athletes
    
    @classmethod
    def find_athlete_by_email(cls, data):
        query= '''
        SELECT *
        FROM athletes
        WHERE email = %(email)s
        ;'''
        result =  connectToMySQL(cls.db).query_db(query, data)
        if result:
            result = cls(result[0])
        return result
    

    @classmethod
    def update_athlete(cls, data):
        print('here I am')
        query = """
        UPDATE athletes
        SET first_name = %(first_name)s, last_name = %(last_name)s,  email = %(email)s
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def get_athlete_by_id(cls, id):
        data= {'id': id}
        query = "SELECT * FROM athletes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])