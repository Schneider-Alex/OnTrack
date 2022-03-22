from dataclasses import dataclass
from email import message
from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for
from flask_app.models import coach, post, event
from flask_app.controllers import coaches

@app.route('/coach/create_post_page/<int:coach_id>')
def create_post_page(coach_id):
    return render_template('create_post.html', coach_id=coach_id)

@app.route('/coach/create_post/<int:coach_id>',methods=['POST'])
def create_post(coach_id):
    post.Post.create_post(request.form)
    print('tried to create post!')
    return redirect('/dashboard')


