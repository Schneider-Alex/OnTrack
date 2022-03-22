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
        data['time'] = cls.parsed_time_data(data['time'])
        if data['athlete_id4']:
            query='''
            INSERT INTO times (time, coach_id, time_id, athlete_id,athlete_id2,athlete_id3,athlete_id4)
            VALUES (%(time)s,%(coach_id)s,%(time_id)s,%(athlete_id)s, %(athlete_id2)s, %(athlete_id3)s, %(athlete_id4)s);'''
        elif data['athlete_id3']:
            query='''
            INSERT INTO times (time, coach_id, time_id, athlete_id,athlete_id2,athlete_id3)
            VALUES (%(time)s,%(coach_id)s,%(time_id)s,%(athlete_id)s, %(athlete_id2)s, %(athlete_id3)s);'''
        elif data['athlete_i2']:
            query='''
            INSERT INTO times (time, coach_id, time_id, athlete_id,athlete_id2)
            VALUES (%(time)s,%(coach_id)s,%(time_id)s,%(athlete_id)s, %(athlete_id2)s);'''
        else:
            query='''
            INSERT INTO times (time, coach_id, time_id, athlete_id)
            VALUES (%(time)s,%(coach_id)s,%(time_id)s, %(athlete_id)s);'''
        return connectToMySQL(cls.db).query_db(query,data)

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
        time_ = data['time'].split(':')
        print(time_)
        #convert to int if needed
        time_ = time_[0] * 60 + time_[1]
        print(time_)
        parsed_data={
            
            'time': time_
            
        }
        return parsed_data  


    #Optional if time: 
    # -group times by date (per athletes, all athletes),  need to add date column to times table in db
    # -group times by athlete

