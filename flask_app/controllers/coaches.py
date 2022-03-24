from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import coach, post, event, athlete, time
from flask_app.controllers import comments, events, posts, times
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if not session:
        return redirect('/')
    roster = False
    if session['coach']:
        # if athlete.Athlete.get_athletes_by_coach_id(session['coach_id']):
            roster=athlete.Athlete.get_athletes_by_coach_id(session['coach_id'])
    elif session['athlete']:
        # if athlete.Athlete.get_all_athletes_teammates(session['coach_id'],session['athlete_id']):
            roster = athlete.Athlete.get_all_athletes_teammates(session['coach_id'],session['athlete_id'])
    return render_template('dashboard.html', coach_posts=post.Post.get_all_coaches_posts(),roster=roster)

@app.route('/coach/register',methods=['POST'])
def coach_registration():
    if coach.Coach.register_coach(request.form):
        coach.Coach.login(request.form)
        return redirect('/dashboard')
    return redirect('/')

@app.route('/coach/login',methods=['POST'])
def coach_login():
    if coach.Coach.login(request.form):
        return redirect('/dashboard')
    return redirect('/')

    
@app.route('/coach/roster/<int:id>')
def view_roster(id):
    roster = athlete.Athlete.get_athletes_by_coach_id(id)
    return render_template('roster.html', athletes = roster)

@app.route('/coach/add_athletes') #from dashboard
def add_athletes():
    return render_template('add_athletes.html')


@app.route('/create_athlete_account', methods=['POST'])
def create_athlete_account():
    print(request.form['first_name'])
    this_athlete = athlete.Athlete.register_athlete(request.form)
    print('>>>>>>>>>>>')
    return redirect(f"/success/{this_athlete}")

@app.route('/success/<int:id>')
def success(id):
    return render_template('success.html', athlete = athlete.Athlete.get_athlete_by_id(id))

@app.route('/coach/update/athlete/display/<int:id>')
def display_for_update(id):
    this_athlete = athlete.Athlete.get_athlete_by_id(id)
    athlete_times = time.Time.get_times_by_athlete_id(id)
    events_ = event.Event.get_all_events()
    print(athlete_times)
    # athlete_times - athlete.Athlete.get  ########## get times by athlete id
    return render_template('update_athlete.html', athlete = this_athlete, athlete_times= athlete_times, events= events_)

@app.route('/coach/update/athlete')
def update_athlete():
    athlete.Athlete.update_athlete(request.form)
    #also need to update times
    return redirect('/') #confirmation page


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



