from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash, session
from flask_app import app
import re, math
from datetime import datetime
from flask_app.models import coach, time
#test 


class Post:
    db = 'on_track'
    def __init__(self, data): 
        self.id = data['id']
        self.content = data['content']
        self.coach_id = data['coach_id']
        self.time_id = data['time_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.time = time.Time.get_time_by_id(self.time_id) 
        # self.time may need some editing and tampering

#displays how long ago post was made
    def timestamp(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    #CREATE
    @classmethod
    def create_post(cls, data):
        # if data['athlete_id4']:
        #     query='''
        #     INSERT INTO posts (content, coach_id, time_id, athlete_id,athlete_id2,athlete_id3,athlete_id4)
        #     VALUES (%(content)s,%(coach_id)s,%(time_id)s,%(athlete_id)s, %(athlete_id2)s, %(athlete_id3)s, %(athlete_id4)s);'''
        # elif data['athlete_id3']:
        #     query='''
        #     INSERT INTO posts (content, coach_id, time_id, athlete_id,athlete_id2,athlete_id3)
        #     VALUES (%(content)s,%(coach_id)s,%(time_id)s,%(athlete_id)s, %(athlete_id2)s, %(athlete_id3)s);'''
        # elif data['athlete_i2']:
        #     query='''
        #     INSERT INTO posts (content, coach_id, time_id, athlete_id,athlete_id2)
        #     VALUES (%(content)s,%(coach_id)s,%(time_id)s,%(athlete_id)s, %(athlete_id2)s);'''
        # else:
        #     query='''
        #     INSERT INTO posts (content, coach_id, time_id, athlete_id)
        #     VALUES (%(content)s,%(coach_id)s,%(time_id)s, %(athlete_id)s);'''
        query="""INSERT INTO posts (content, coach_id, time_id)
        VALUES (%(content)s,%(coach_id)s,%(time_id)s);
        """
        return connectToMySQL(cls.db).query_db(query,data)

    #READ
    @classmethod
    def get_all_posts(cls, id):
        query='''SELECT * FROM posts
        WHERE coach_ id = %(coach_id)s;'''  

        result= connectToMySQL(cls.db).query_db(query, data)
        if result:
            posts=[]
            for m in result:
                posts.append(cls(m))
            return posts
        return result

    @classmethod
    def get_all_coaches_posts(cls):
        
        data={"coach_id": session['coach_id']}
        query='''SELECT * FROM posts
        WHERE coach_id = %(coach_id)s;'''  

        result= connectToMySQL(cls.db).query_db(query, data)
        if result:
            posts=[]
            for m in result:
                posts.append(cls(m))
            return posts
        return result

    @classmethod
    def get_post_by_id(cls, id):
        data= {'id': id}
        query = '''SELECT * FROM posts WHERE id = %(id)s;'''
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def update_post(cls, data):
        data={
            'content' : data['content'],
            'id' : data['id']
        }
        query = """
        UPDATE posts
        SET content = %(content)s, updated_at = NOW()
        WHERE id = %(id)s
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def delete_post(cls, id):
        data ={ "id" : id}
        query="""
        DELETE FROM likes WHERE post_id= %(id)s
        """
        connectToMySQL(cls.db).query_db(query, data)
        query="""
        DELETE FROM comments WHERE post_id= %(id)s
        """
        connectToMySQL(cls.db).query_db(query, data)
        query= '''
        DELETE FROM posts
        WHERE id = %(id)s
        ;'''
        print('made ','it')
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def athlete_like_post(cls,post_id):
        data={
            'athlete_id' : session['athlete_id'],
            'post_id' : post_id
        }
        query = """
        INSERT INTO likes
        (athlete_id, post_id) values (%(athlete_id)s,%(post_id)s)
        ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return result