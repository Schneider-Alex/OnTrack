
from asyncio import events
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for, jsonify
from flask_app.models import coach
from flask_app.controllers import coaches

class Event:
    db = 'on_track'
    def __init__(self, data): 
        self.id = data['id']
        self.name = data['name']


    #CREATE
    @classmethod
    def create_times(cls, data):
        query='''INSERT INTO times (name)
            VALUES (%(name)s;'''
        return connectToMySQL(cls.db).query_db(query,data)


    #read

    @classmethod
    def get_all_events(cls):
        query='''SELECT * FROM events''' ######May have to add coach_id
        results = connectToMySQL(cls.db).query_db(query)
        if len(results) < 1:
            return False
        events = []
        for row in results:
            events.append(cls(row))
        return events
    