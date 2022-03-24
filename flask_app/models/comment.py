from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
import re, math
from datetime import datetime
from flask_app.models import coach, event, post,comment_content
#test 


class Comment:
    db = 'on_track'
    def __init__(self, data): 
        self.id = data['id']
        self.comment = comment_content.Comment_content.get_content_by_id(data['comment'])
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
        data = {
            'comment':data['comment'],
            'user_id':data['user_id'],
            'post_id':data['post_id']
        }
        query='''
        INSERT INTO comments (comment_content_id, athlete_id, post_id)
        VALUES (%(comment)s,%(user_id)s,%(post_id)s);''' # will need hidden input with post id when sending comment
        return connectToMySQL(cls.db).query_db(query,data)


#REad
    @classmethod
    def get_all_comments(cls, id):
        data= {'id' : id}
        query='''SELECT *
        FROM comments
        LEFT JOIN athletes ON athletes.id = comments.athlete_id
        LEFT JOIN posts ON posts.id = comments.post_id 
        WHERE post_id = %(id)s;''' 
        result = connectToMySQL(cls.db).query_db(query,data)
        if len(result)<1:
            return
        else:
            comments = []
            for row in result:
                this_comment = {
                    'id':row['id'],
                    'comment': row['comment_content_id'],
                    'user_id': row['athlete_id'],
                    'post_id':row['post_id'],
                    'created_at':row['created_at'],
                    'updated_at':row['updated_at']
                }
                comments.append(Comment(this_comment))
            print(comments,"$$$$$$$$$$$$$")
            return (comments) 


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