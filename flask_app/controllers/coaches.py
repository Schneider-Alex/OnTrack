from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import coach, post, event, athlete
from flask_app.controllers import comments, events, posts
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



# *************JUST REDIRECTING ALL METHODS TO ROOT ROUTE FOR NOW (SUBJECT TO CHANGE)****************

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coach/register',methods=['POST'])
def coach_registration():
    if coach.Coach.register_coach(request.form)
        coach.Coach.login(request.form)
    return redirect('/')
    
@app.route('/coach/create/athlete_account',methods=['POST'])
def create_athlete_account():
    athlete.Athlete.register_athlete(request.form)
    return redirect('/')

@app.route('/coach/login',methods=['POST'])
def coach_login():
    coach.Coach.login(request.form)
    return redirect('/')
