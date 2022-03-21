from datetime import datetime, date
from time import gmtime, strftime
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash, session
from flask_app import app
import re	# the regex module
from flask_bcrypt import Bcrypt   
from flask_app.models import coach, post, time  


class Event:
    db ='OnTrackERD'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        


#CREATE
    @classmethod
    def create_event(cls, data):
        data = cls.parse_location(data)
        query='''
        INSERT INTO events (name)
        VALUES (%(name)s);''' # will need hidden input with recipient id when sending message
        
        return connectToMySQL(cls.db).query_db(query,data)

    

#Read

    @classmethod
    def get_all_events(cls): 
        query = """
        SELECT *
        FROM events
        ;"""
        result = connectToMySQL(cls.db).query_db(query)
        events = []
        for row in result:
            events.append(cls(row))
        return events



    @classmethod
    def get_by_id(cls, id):
        data = {'id' : id}
        query = '''SELECT * FROM events
                WHERE id = %(id)s
                ;'''
        results = connectToMySQL(cls.db).query_db(query,data)
        # print(results)
        if len(results) < 1:
            return False
        return cls(results[0])



    #not sure if this will be needed
    @classmethod
    def get_events_by_user_id(cls,id):
        data = {'user_id' : id}
        query = '''SELECT * FROM events
                WHERE user_id = %(user_id)s
                ;'''   ###May need to revise query
        result = connectToMySQL(cls.db).query_db(query,data)
        events = []
        for row in result: 
            events.append(cls(row))
        # print(events)
        return events

    
    #UPDATE

    @classmethod
    def update_by_id(cls, data):
        query = """
        UPDATE events
        SET name = %(name)s
        WHERE events.id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    
    #DELETE
    @classmethod
    def delete_event(cls,id):
        data = { 'id' : id }
        query = """
        DELETE FROM events
        WHERE id = %(id)s
        ;""" # * in delete query
        return connectToMySQL(cls.db).query_db(query, data)



########### VALIDATE EVENT !!!!!!!!!!!!!!!!!
    @classmethod
    def validate_event(cls, data):
        data = cls.parse_location(data) #could make as cls method and put here one time instead of contollers multiple times
        is_valid = True # assume true
        if len(data['name']) < 5:
            flash('Name must be 5 or more characters', 'event')
            is_valid = False
        return is_valid



