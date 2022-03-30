from unittest import result
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask import flash, session
from flask_app.models import event, post, time, athlete    
import csv 


class Time:
    db = 'on_track'
    def __init__(self, data): 
        self.id = data['id']
        self.time = data['time'] # + (data['minutes'] * 60)  --use dropdown for minutes
        self.date =data['date']
        self.athlete_id = data['athlete_id']
        self.coach_id = data['coach_id']
        self.event_id= data['event_id']
        self.event = data['event']
        time = self.convert_time(self.time)
        self.time= time['formatted']
        self.minutes = time['minutes']
        self.seconds = time['seconds']
        self.athlete = athlete.Athlete.get_athlete_by_id(self.athlete_id)
        
    #CREATE
    @classmethod
    def create_times(cls, data):
        #Can add validation so same names are not picked more than once( use a set function to make just unique values then compare length)
                #--Also no ensure events has 'relay' in it (can do with event id match)
        # data['time'] = cls.parsed_time_data(data['time'])
        #if minutes entered:  run method to convert
        # data = {time = data['time] + (data['minutes'] * 60)  --use dropdown for minutes
        # if data['minutes'] != '':
        #     data['time'] = data['time'] + data['minutes'] * 60
        data = cls.parsed_time_data(data)
        if data['isRelay'] == '1':
            query='''
            INSERT INTO times (time,  date, coach_id, event_id, athlete_id,athlete_id2,athlete_id3,athlete_id4)
            VALUES (%(time)s, %(date)s, %(coach_id)s, %(event_id)s, %(athlete_id)s, %(athlete_id2)s, %(athlete_id3)s, %(athlete_id4)s);'''
        else:
            query='''
            INSERT INTO times (time, date, coach_id, athlete_id, event_id)
            VALUES (%(time)s, %(date)s, %(coach_id)s, %(athlete_id)s, %(event_id)s);'''
        return connectToMySQL(cls.db).query_db(query,data)

    #READ
    @classmethod
    def get_time_by_athlete_id(cls, id):
        data = {
            'id':id
        }
        query = """
        SELECT * FROM times
        LEFT JOIN athletes ON athletes.id = times.athlete_id
        LEFT JOIN events ON events.id = times.event_id
        LEFT JOIN coaches ON coaches.id = times.coach_id
        WHERE athlete_id = %(id)s OR athlete_id2 = %(id)s OR athlete_id3 = %(id)s OR athlete_id4 = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results)<1:
            return False
        else:
            times = []
            for row in results:
                this_time={
                    'id':row['id'],
                    'time':row['time'],
                    'athlete_id':row['athlete_id'],
                    'coach_id':row['coach_id'],
                    'event_id':row['event_id'],
                    'event':row['name'],
                    'date':row['date']
                }
                
                times.append(Time(this_time))
            return times


    @classmethod
    def get_times_by_event_id(cls, id ):
        data= {'id' : id,
        'coach_id': session['coach_id']}
        query='''
        SELECT times.*, events.*, athletes.* FROM times
        JOIN events ON events.id = times.event_id
        JOIN athletes ON athletes.id = times.athlete_id
        WHERE events.id = %(id)s AND times.coach_id =%(coach_id)s'''
        
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        if len(results) < 1:
            return results
        #Use AJAX to display vs. make instances
        #will also need coach id
        #allows coach and students to view top results have order by functionality for ordering by last name, time length
        #What about relays?

    # @classmethod
    # def get_times_by_athlete_id(cls, id):
    #     data = {'athlete_id': id,
    #             'coach_id' : session['coach_id']}
    #     query = '''SELECT times.time, times.date, times.id, times.event_id, events.name  FROM times
    #     JOIN events ON events.id = times.event_id
    #     WHERE times.athlete_id = %(athlete_id)s
    #     AND times.coach_id = %(coach_id)s;'''
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     print(results)
    #     if len(results) < 1:
    #         return results
    #     times=[]
    #     for row in results:
    #         this_time = {'time': row['time'],
    #                     'name': row['name'],
    #                     'date' : row['date'],
    #                     'id' : row['id']
    #                     }
    #         times.append(this_time)
    #     print('!!!!!@@@@', times)
    #     return times
    #coach id in hidden input

    @classmethod
    def get_best_by_event_and_athlete(cls, athlete_id, event_id):
        data = {
            'athlete_id' : athlete_id,
            'event_id': event_id
        }
        query = """
        SELECT times.*, events.*, athletes.* FROM times
        JOIN events ON events.id = times.event_id
        JOIN athletes ON athletes.id = times.athlete_id
        WHERE events.id = %(event_id)s AND times.athlete_id =%(athlete_id)s OR events.id = %(event_id)s AND times.athlete_id2 =%(athlete_id)s OR events.id = %(event_id)s AND times.athlete_id3 =%(athlete_id)s OR events.id = %(event_id)s AND times.athlete_id4 =%(athlete_id)s
        ORDER BY times.time ASC
        LIMIT 1;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            this_time={
                    'id':results[0]['id'],
                    'time':results[0]['time'],
                    'athlete_id':results[0]['athlete_id'],
                    'coach_id':results[0]['coach_id'],
                    'event_id':results[0]['event_id'],
                    'event':results[0]['name'],
                    'date':results[0]['date']
                }
            return cls(this_time)
        else:
            return 
    
    @classmethod
    def get_best_by_event_and_coach(cls, coach_id, event_id):
        data = {
            'coach_id' : coach_id,
            'event_id': event_id
        }
        query = """
        SELECT times.*, events.*, athletes.* FROM times
        JOIN events ON events.id = times.event_id
        JOIN athletes ON athletes.id = times.athlete_id
        WHERE events.id = %(event_id)s AND times.coach_id =%(coach_id)s
        ORDER BY times.time ASC
        LIMIT 1;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            this_time={
                    'id':results[0]['id'],
                    'time':results[0]['time'],
                    'athlete_id':results[0]['athlete_id'],
                    'coach_id':results[0]['coach_id'],
                    'event_id':results[0]['event_id'],
                    'event':results[0]['name'],
                    'date':results[0]['date']
                }
            return cls(this_time)
        else:
            return 

    @classmethod
    def get_team_records(cls, coach_id):
        data = {
            'coach_id' : coach_id,
        }
        query = """
        SELECT DISTINCT times.event_id, times.coach_id FROM times
        JOIN events ON events.id = times.event_id
        JOIN coaches ON times.coach_id = coaches.id
        JOIN athletes ON athletes.id = times.athlete_id
        WHERE times.coach_id =%(coach_id)s
        ORDER BY times.event_id ASC
        ;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        
        if result:
            times = []
            for row in result:
                this_time = cls.get_best_by_event_and_coach(row['coach_id'], row['event_id'])
                times.append(this_time)
            print(times, '$$$$$')
            # times = cls.get_top_only(times)
            return times
        else:
            return 


    #UPDATE
    @classmethod
    def update_time(cls, data):
        data = cls.parsed_time_data_update(data)
        query='''UPDATE times
        SET time = %(time)s, date = %(date)s,  event_id = %(event_id)s
        WHERE id = %(athlete_id)s'''
        result = connectToMySQL(cls.db).query_db(query, data)
        print('>>>>>>>>>',result)
        return result

    @classmethod
    def convert_time(cls,time):
        seconds = time%60
        minutes = int((time-seconds)/60)
        if minutes<1:
            time_dict = {
                'formatted': f"{seconds}",
                'minutes': minutes,
                'seconds': seconds
            }
            return time_dict
        if seconds<10:
            time_dict = {
                'formatted': f"{minutes}:0{seconds}",
                'minutes': minutes,
                'seconds': seconds
            }
            return time_dict
        time_dict = {
                'formatted': f"{minutes}:{seconds}",
                'minutes': minutes,
                'seconds': seconds
            }
        return time_dict

    @classmethod
    def delete_time(cls, id):
        pass

    @classmethod
    def search_times_factors_coach_id(cls, data ):
        #All factors selected
        if data['date'] != '' and data['athlete_id'] != '' and data['event_id'] != '':
            query='''
            SELECT times.*, events.*, athletes.* FROM times
            JOIN events ON events.id = times.event_id
            JOIN athletes ON athletes.id = times.athlete_id
            WHERE events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND date = %(date)s AND times.athlete_id= %(athlete_id)s
            OR events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND times.athlete_id2= %(athlete_id)s
            OR events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND times.athlete_id3= %(athlete_id)s
            OR events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND times.athlete_id4= %(athlete_id)s'''
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return 'No time found'
            print(results, '$$$$$$$$$$$$$$$$$')
            
            return results
    ### No date selected
        if data['date'] == '' and data['athlete_id'] != '' and data['event_id'] != '':
            query='''
            SELECT times.*, events.*, athletes.* FROM times
            JOIN events ON events.id = times.event_id
            JOIN athletes ON athletes.id = times.athlete_id
            WHERE events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND times.athlete_id= %(athlete_id)s 
            OR events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND times.athlete_id2= %(athlete_id)s
            OR events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND times.athlete_id3= %(athlete_id)s
            OR events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND times.athlete_id4= %(athlete_id)s'''
        
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return 'No time found'
            if int(data['event_id']) > 3 and int(data['event_id']) < 8 :
                results = cls.relay_names(results)
            return results

            ##No athlete selected
        if data['date'] != '' and data['athlete_id'] == '' and data['event_id'] != '':
            query='''
            SELECT times.*, events.*, athletes.* FROM times
            JOIN events ON events.id = times.event_id
            JOIN athletes ON athletes.id = times.athlete_id
            WHERE events.id = %(event_id)s AND times.coach_id =%(coach_id)s AND date = %(date)s'''
        
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return 'No time found'
            if int(data['event_id']) > 3 and int(data['event_id']) < 8 :
                results = cls.relay_names(results)

            return results

    ### no date or athlete >>> event only
        if data['date'] == '' and data['athlete_id'] == '' and data['event_id'] != '':
            query='''
            SELECT times.*, events.*, athletes.* FROM times
            JOIN events ON events.id = times.event_id
            JOIN athletes ON athletes.id = times.athlete_id
            WHERE events.id = %(event_id)s AND times.coach_id =%(coach_id)s'''
        
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return 'No time found'
            
            if int(data['event_id']) > 3 and int(data['event_id']) < 8 :
                results = cls.relay_names(results)
            print(results)
            return results
        #### no event or date........Athlete only
        if data['date'] == '' and data['athlete_id'] != '' and data['event_id'] == '':
            query='''
            SELECT times.*, events.*, athletes.* FROM times
            JOIN athletes ON athletes.id = times.athlete_id
            JOIN events ON events.id = times.event_id
            WHERE times.athlete_id= %(athlete_id)s AND times.coach_id =%(coach_id)s
            OR times.coach_id =%(coach_id)s AND times.athlete_id2= %(athlete_id)s
            OR times.coach_id =%(coach_id)s AND times.athlete_id3= %(athlete_id)s
            OR times.coach_id =%(coach_id)s AND times.athlete_id4= %(athlete_id)s'''
        
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return 'No time found'
            print(results)
            for row in results:
                if int(row['event_id']) > 3 and int(row['event_id']) < 8 :
                    row = cls.relay_names(row)
            return results

        ###### no event or athlete>>>>>Date Only
        if data['date'] != '' and data['athlete_id'] == '' and data['event_id'] == '':
            query='''
            SELECT times.*, events.*, athletes.* FROM times
            JOIN events ON events.id = times.event_id
            JOIN athletes ON athletes.id = times.athlete_id
            WHERE date = %(date)s AND times.coach_id =%(coach_id)s'''
        
            results = connectToMySQL(cls.db).query_db(query, data)
            if len(results) < 1:
                return 'No time found'
            print(results)
            for row in results:
                if int(row['event_id']) > 3 and int(row['event_id']) < 8 :
                    print(row)
                    row = cls.relay_names(row)
            return results
      
    @classmethod
    def relay_names(cls, data):
        if type(data) == list:
            for row in data:
                row['athlete2'] = athlete.Athlete.get_athlete_by_id(row['athlete_id2']).full_name
                row['athlete3'] = athlete.Athlete.get_athlete_by_id(row['athlete_id3']).full_name
                row['athlete4'] = athlete.Athlete.get_athlete_by_id(row['athlete_id4']).full_name
        else:
            data['athlete2'] = athlete.Athlete.get_athlete_by_id(data['athlete_id2']).full_name
            data['athlete3'] = athlete.Athlete.get_athlete_by_id(data['athlete_id3']).full_name
            data['athlete4'] = athlete.Athlete.get_athlete_by_id(data['athlete_id4']).full_name
        return data

    @staticmethod
    def validate_time(data):
        is_valid = True
        # if float(data['time']) < 0 or float(data['time']) > 3000:
        #     flash('valid times must be greater than 1 and less than 3,000 seconds', 'time')
        #     is_valid = False
        if data['date'] == '': 
            flash('must enter date', 'event')
            is_valid = False
        if data['isRelay'] == '1':  
            if data['athlete_id'] == data['athlete_id2'] or data['athlete_id3']  == data['athlete_id4']:
                flash('Cannot have duplicate athletes', 'time')
                is_valid = False
            if int(data['event_id']) not in [5, 6, 7, 8, 17, 18, 19, 20]:
                flash('Event must be a relay', 'time')
                is_valid = False
        return is_valid
        
    @staticmethod
    def parsed_time_data(data):
        time_ = float(data['time']) + float(data['minutes']) * 60
        print(time_)
        parsed_data={
            'date':data['date'],
            'time': time_,
            'coach_id': data['coach_id'],
            'athlete_id': data['athlete_id'],
            'event_id': data['event_id'],
            'isRelay' : data['isRelay']
        }
        if data['isRelay'] == '1':
            parsed_data['athlete_id2'] = data['athlete_id2']
            parsed_data['athlete_id3'] = data['athlete_id3']
            parsed_data['athlete_id4'] = data['athlete_id4']
        return parsed_data  

    @staticmethod
    def parsed_time_data_update(data):
        time_ = float(data['seconds']) + float(data['minutes'] * 60)
        print(time_)
        parsed_data={
            'date':data['date'],
            'time': time_,
            'coach_id': data['coach_id'],
            'athlete_id': data['athlete_id'],
            'event_id': data['event_id'],
            'isRelay' : data['isRelay']
        }
        if data['isRelay'] == '1':
            parsed_data['athlete_id2'] = data['athlete_id2']
            parsed_data['athlete_id3'] = data['athlete_id3']
            parsed_data['athlete_id4'] = data['athlete_id4']
        return parsed_data  
    #Optional if time: 
    # -group times by date (per athletes, all athletes),  need to add date column to times table in db
    # -group times by athlete

    @staticmethod
    def get_top_only(arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i].event == arr[j].event:
                    arr.pop(arr[j])
        return arr

    # @classmethod
    # def write_csv(cls, id):
    #     data= {'id' : id,
    #     'coach_id': session['coach_id']}
    #     # get times by event
    #     query='''
    #     SELECT times.*, events.*, athletes.* FROM times
    #     JOIN events ON events.id = times.event_id
    #     JOIN athletes ON athletes.id = times.athlete_id
    #     WHERE event.id = %(id)s AND times.coach_id =%(coach_id)s'''
        
    #     results = connectToMySQL(cls.db).query_db(query, data)

    #     c = csv.writer(open("temp.csv","wb"))
    #     for row in results:
    #         c.writerow(row)
    #     c.close()
    
    # @classmethod
    # def write_pdf(cls, id):
    #     data= {'id' : id,
    #     'coach_id': session['coach_id']}
    #     # get times by event
    #     query='''
    #     SELECT times.*, events.*, athletes.* FROM times
    #     JOIN events ON events.id = times.event_id
    #     JOIN athletes ON athletes.id = times.athlete_id
    #     WHERE events.id = %(id)s AND times.coach_id =%(coach_id)s'''
        
    #     results = connectToMySQL(cls.db).query_db(query, data)

        

        