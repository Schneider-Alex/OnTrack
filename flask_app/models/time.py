from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask import flash, session
from flask_app.models import event, post, time     


class Time:
    db = 'on_track'
    def __init__(self, data): 
        self.id = data['id']
        self.time = data['time']
        self.athlete_id = data['athlete_id']
        self.coach_id = data['coach_id']
        self.event_id= data['event_id']

    def time_display(self, time):
        pass
    #convert time to track time

    
    #CREATE
    @classmethod
    def create_times(cls, data):
        data = cls.parsed_time_data(data)
        query= '''
        Insert INTO coaches (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s,%(password)s)
        ;'''
        coach_id = connectToMySQL(cls.db).query_db(query,data)
        session['coach_id'] = coach_id
        session['first_name'] = data['first_name']
        # session['coach']=True
        # removed this functionality so that coaches must log in after creating account
        return coach_id

    #READ
    
    @classmethod
    def get_times_by_event_id(cls, id ):
        data= {'id' : id}
        #will also need coach id
        #allows coach and students to view top results have order by functionality for ordering by last name, time length

    @classmethod
    def get_times_by_athlete_id(cls, data):
        query = '''SELECT * FROM times
        JOIN events ON events.id = times.event_id
        WHERE times.athlete_id = %(athlete_id)s
        AND times.coach_id = %(coach_id)s;'''
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    #will need coach id (use session in hidden input or include a parse data function)
   
    @classmethod
    def desc_times_by_event(cls, id):
        pass

    @staticmethod
    def parsed_time_data(data):
        parsed_data={
            'athlete_id': data['athlete_id'],
            'time': data['time'].strip(),
            'coach_id' : session['coach_id'],
            'event_id' : data['event_id']
        }
        return parsed_data  


    #Optional if time: 
    # -group times by date (per athletes, all athletes),  need to add date column to times table in db
    # -group times by athlete

