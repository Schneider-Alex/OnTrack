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
    return redirect('/dashboard')

@app.route('/post/<int:post_id>/delete')
def delete_post(post_id):
    post.Post.delete_post(post_id)
    return redirect('/dashboard')

@app.route('/post/<int:post_id>/edit_page')
def edit_post_page(post_id):
    return render_template('update_post.html', post=post.Post.get_post_by_id(post_id))

@app.route('/post/edit',methods=['POST'])
def edit_post():
    
    return render_template('/dashboard')

