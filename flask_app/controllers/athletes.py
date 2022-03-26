from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for, jsonify
from flask_app.models import coach, post, event, athlete, time
from flask_app.controllers import comments, events, posts,coaches, times
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/athlete/login',methods=['POST'])
def athlete_login():
    if athlete.Athlete.login(request.form):
        return redirect('/dashboard')
    return redirect ('/')

@app.route('/athletes/get_all') #This is for ajax, athlete drop down
def get_all_athletes_by_coach_id_ajax():
    athletes = athlete.Athlete.get_athletes_by_coach_id_ajax(session["coach_id"])
    #cannot jsonify instance amke new method
    return jsonify (athletes = athletes)


    
@app.route('/athlete/view/<int:id>')
def athlete_view_info(id):
    this_athlete = athlete.Athlete.get_athlete_by_id(id)
    athletes_times = time.Time.get_time_by_athlete_id(id)
    return render_template('view_athlete_info.html', athlete=this_athlete, times=athletes_times)

@app.route('/athlete/view/teammate/<int:id>')
def view_teammate(id):
    this_athlete = athlete.Athlete.get_athlete_by_id(id)
    athletes_events = event.Event.get_events_by_user_id(id)
    times = []
    
    for race in athletes_events:
        times.append(time.Time.get_best_by_event_and_athlete(id, race.id))
    print(times, "$$$$$$$$$$$$$$")
    return render_template('view_athlete_info.html', athlete=this_athlete, times=times)
    