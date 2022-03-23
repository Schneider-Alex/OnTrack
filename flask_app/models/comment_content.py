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
            SELECT * FROM comment_content
        """
        return connectToMySQL(cls.db).query_db(query)