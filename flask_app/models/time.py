from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app

class Time:
    db = 'on_track'
    def __init__(self, data): 
        self.id = data['id']