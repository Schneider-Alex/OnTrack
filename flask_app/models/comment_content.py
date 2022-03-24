from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
import re, math
from datetime import datetime
from flask_app.models import coach, event, post, comment

class Comment_content:
    db = 'on_track'
    def __init__(self, data):
        self.id = data['id']
        self.content = data['id']
    
    @classmethod
    def get_all_comments(cls): 
        query = """
            SELECT * FROM comment_content;
        """
        result = connectToMySQL(cls.db).query_db(query)
        all_content = []
        for row in result:
            this_content = {
                'id':row['id'],
                'content':row['content']
            }
            all_content.append(this_content)
        return all_content
    @classmethod
    def get_content_by_id(cls,id):
        print(id,"^^^^^^^^^^^^^^^^^^^^")
        data ={
            'id':id
        }
        query = """
            SELECT * FROM comment_content
            WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result[0]['content'], "##############")
        return result[0]['content']