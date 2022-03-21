from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import coach, post, event, athlete
from flask_app.controllers import comments, events, posts
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/athlete/login',methods=['POST'])
def athlete_login():
    athlete.Athlete.login(request.form)
    return redirect('/')