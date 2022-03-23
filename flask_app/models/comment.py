from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
import re, math
from datetime import datetime
from flask_app.models import coach, event, post
#test 


class Comment:
    db = 'on_track'
    def __init__(self, data): 
        self.id = data['id']
        self.comment = data['comment']
        self.user_id = data['user_id']
        # self.event_id = data['event_id']#should change to sender (it will have all the info)
        # self.recipient_id = data['recipient_id']
        # self.recipient = data['recipient']
        # Should only need comment content, user_id of athlete, and post_id for the comments
        self.post_id = data['post_id']
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
        INSERT INTO comments (comment, user_id, post_id)
        VALUES (%(comment)s,%(user_id)s,%(post_id)s);''' # will need hidden input with post id when sending comment
        return connectToMySQL(cls.db).query_db(query,data)


#REad
    @classmethod
    def get_all_comments(cls, id):
        data= {'id' : id}
        query='''SELECT *
        FROM comments
        LEFT JOIN users ON users.id = comments.user_id
        LEFT JOIN posts ON posts.id = comments.post_id 
        WHERE posts.id = %(id)s;''' 
        return connectToMySQL(cls.db).query_db(query,data)

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