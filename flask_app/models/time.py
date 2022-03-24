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
            VALUES (CAST(%(time)s AS DECIMAL(5,3)), %(date)s, %(coach_id)s, %(athlete_id)s, %(event_id)s);'''
        return connectToMySQL(cls.db).query_db(query,data)

    #READ
    @classmethod
    def get_time_by_id(cls, id):
        data = {
            'id':id
        }
        query = """
        SELECT * FROM times
        LEFT JOIN athletes ON athletes.id = times.athlete_id
        LEFT JOIN events ON events.id = times.event_id
        LEFT JOIN coaches ON coaches.id = times.coach_id
        WHERE athlete_id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results)<1:
            return
        else:
            times = []
            for row in results:
                this_time={
                    'id':row['id'],
                    'time':row['time'],
                    'athlete_id':row['athlete_id'],
                    'coach_id':row['coach_id'],
                    'event_id':row['event_id']
                }
                times.append(Time(this_time))
            return times


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
        query = '''SELECT times.time, times.date, times.id, times.event_id, events.name  FROM times
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
                        'date' : row['date'],
                        'id' : row['id']
                        }
            times.append(this_time)
        print('!!!!!@@@@', times)
        return times
    #coach id in hidden input
   
    @classmethod
    def desc_times_by_event(cls, id):
        pass


    #UPDATE
    @classmethod
    def update_time(cls, data):
        query='''UPDATE times
        SET time = %(time)s, date = %(date)s,  event_id = %(event_id)s
        WHERE id = %(id)s'''
        result = connectToMySQL(cls.db).query_db(query, data)
        print('>>>>>>>>>',result)
        return result

    @classmethod
    def delete_time(cls, id):
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

