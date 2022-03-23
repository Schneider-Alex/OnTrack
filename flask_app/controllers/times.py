from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import coach, time, athlete, post, event
from flask_app.controllers import coaches, athletes, posts, events

#CREATE
@app.route('/coach/create/times')
def create_times_page():
    athletes_ = athlete.Athlete.get_athletes_by_coach_id(session['coach_id'])
    events_ = event.Event.get_all_events()
    return render_template('create_times.html', athletes = athletes_, events = events_)

@app.route('/create/new/time', methods=['POST'])
def create_new_times():
    print(request.form)
    time.Time.create_times(request.form)
    return redirect('/dashboard')

#READ
#render View time page

#UPDATE
@app.route('/time/update', methods=['POST'])
def update_time():
    time.Time.update_time(request.form)
    print('$$$$$$', request.form)
    return redirect('/success_updated_time')

@app.route('/success_updated_time')
def success_update():
    return render_template('success_updated_time.html')


