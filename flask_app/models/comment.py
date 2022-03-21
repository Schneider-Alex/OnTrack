from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
import re, math
from datetime import datetime
from flask_app.models import coach, event
#test 


class Comment:
    db = 'OnTrackERD'
    def __init__(self, data): 
        self.id = data['id']
        self.comment = data['comment']
        self.user_id = data['user_id']
        self.event_id = data['event_id']#should change to sender (it will have all the info)
        self.recipient_id = data['recipient_id']
        self.recipient = data['recipient']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#notice that timestamp is an instance method, not a class
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

#Create
    #CREATE
    @classmethod
    def create_comment(cls, data):
        query='''
        INSERT INTO comments (comment, user_id, event_id)
        VALUES (%(comment)s,%(user_id)s,%(event_id)s);''' # will need hidden input with event id when sending comment
        return connectToMySQL(cls.db).query_db(query,data)


#REad
    @classmethod
    def get_all_comments(cls, id):
        data= {'id' : id}
        query='''SELECT *
        FROM comments
        LEFT JOIN users ON users.id = comments.user_id
        LEFT JOIN events ON events.id = comments.event_id 
        WHERE events.id = %(id)s;''' 


#Update

    #DELETE
    @classmethod
    def delete_comment(cls, id):
        data ={ "id" : id}
        query= '''
        DELETE FROM comments
        WHERE id = %(id)s
        ;'''
        print('made ','it')
        return connectToMySQL(cls.db).query_db(query, data)


    ###Validation
    #len>10