from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import coach, post, event, athlete, time
from flask_app.controllers import comments, events, posts,coaches, times
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/athlete/login',methods=['POST'])
def athlete_login():
    if athlete.Athlete.login(request.form):
        return redirect('/dashboard')
    return redirect ('/')
    
@app.route('/athlete/view/<int:id>')
def athlete_view_info(id):
    this_athlete = athlete.Athlete.get_athlete_by_id(id)
    athletes_times = time.Time.get_time_by_id(id)
    return render_template('view_athlete_info.html', athlete=this_athlete, times=athletes_times)