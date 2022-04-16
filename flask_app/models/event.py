from datetime import datetime, date
from time import gmtime, strftime
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash, session
from flask_app import app
import re	# the regex module
from flask_bcrypt import Bcrypt   
from flask_app.models import coach, post, time  


class Event:
    db = 'on_track'
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

    @classmethod
    def get_events_by_user_id(cls,id):
        data = {'user_id' : id}
        query = '''
                SELECT DISTINCT event_id, events.name
                FROM times
                LEFT JOIN athletes ON athletes.id = times.athlete_id
                LEFT JOIN events ON events.id = times.event_id
                LEFT JOIN coaches ON coaches.id = times.coach_id
                WHERE athlete_id = %(user_id)s OR athlete_id2 = %(user_id)s  OR athlete_id3 = %(user_id)s OR athlete_id4 = %(user_id)s 
                ;'''   
        result = connectToMySQL(cls.db).query_db(query,data)
        events = []
        if result:
            for row in result: 
                this_event = {
                    'id': row['event_id'],
                    'name': row['name']
                }
                events.append(cls(this_event))
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
        ;""" 
        return connectToMySQL(cls.db).query_db(query, data)



########### VALIDATE EVENT !!!!!!!!!!!!!!!!!
    @classmethod
    def validate_event(cls, data):
        data = cls.parse_location(data) 
        is_valid = True # assume true
        if len(data['name']) < 5:
            flash('Name must be 5 or more characters', 'event')
            is_valid = False
        return is_valid



