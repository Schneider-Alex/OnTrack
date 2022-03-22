from unittest import result
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
        # data['time'] = cls.parsed_time_data(data['time'])
        # if data['athlete_id4']:
        #     query='''
        #     INSERT INTO times (time,  date, coach_id, event_id, athlete_id,athlete_id2,athlete_id3,athlete_id4)
        #     VALUES (%(time)s,%(coach_id)s, %(date)s, %(event_id)s, %(athlete_id)s, %(athlete_id2)s, %(athlete_id3)s, %(athlete_id4)s);'''
        # elif data['athlete_id3']:
        #     query='''
        #     INSERT INTO times (time, date, coach_id, event_id, athlete_id,athlete_id2,athlete_id3)
        #     VALUES (%(time)s, %(date)s, %(coach_id)s, %(event_id)s, %(athlete_id)s, %(athlete_id2)s, %(athlete_id3)s);'''
        # elif data['athlete_i2']:
        #     query='''
        #     INSERT INTO times (time, date, coach_id, event_id, athlete_id,athlete_id2)
        #     VALUES (%(time)s, %(date)s, %(coach_id)s, %(event_id)s, %(athlete_id)s, %(athlete_id2)s);'''
        # else:
        #     query='''
        #     INSERT INTO times (time, date, coach_id, event_id, athlete_id)
        #     VALUES (%(time)s, %(date)s, coach_id)s, %(athlete_id)s), %(event_id)s;'''
        query='''
            INSERT INTO times (time, date, coach_id, athlete_id, event_id)
            VALUES (%(time)s, %(date)s, %(coach_id)s, %(athlete_id)s, %(event_id)s);'''
        return connectToMySQL(cls.db).query_db(query,data)

    #READ
    @classmethod
    def get_time_by_id(cls, id):
        pass


    @classmethod
    def get_times_by_event_id(cls, id ):
        data= {'id' : id,
        'coach_id': session['coach_id']}
        #will also need coach id
        #allows coach and students to view top results have order by functionality for ordering by last name, time length

    @classmethod
    def get_times_by_athlete_id(cls, id):
        data = {'athlete_id': id,
                'coach_id' : session['coach_id']}
        query = '''SELECT times.time, times.date, events.name FROM times
        JOIN events ON events.id = times.event_id
        WHERE times.athlete_id = %(athlete_id)s
        AND times.coach_id = %(coach_id)s;'''
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        if len(results) < 1:
            return results
        times=[]
        for row in results:
            this_time = {'time': row['time'],
                        'name': row['name'],
                        'date' : row['date']}
            times.append(this_time)
        
        return times
    #coach id in hidden input
   
    @classmethod
    def desc_times_by_event(cls, id):
        pass

    # @staticmethod
    # def parsed_time_data(data):
    #     time_ = data['time'].split(':')
    #     print(time_)
    #     #convert to int if needed
    #     time_ = time_[0] * 60 + time_[1]
    #     print(time_)
    #     parsed_data={
            
    #         'time': time_
            
    #     }
    #     return parsed_data  


    #Optional if time: 
    # -group times by date (per athletes, all athletes),  need to add date column to times table in db
    # -group times by athlete

