from dataclasses import dataclass
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import athlete, coach, post, comment, comment_content
from flask_app.controllers import athletes, coaches

@app.route('/post/<int:post_id>/comment')
def show_post(post_id):
    this_post = post.Post.get_post_by_id(post_id)
    all_comment_content = comment_content.Comment_content.get_all_comments()
    all_comments = comment.Comment.get_all_comments(post_id)
    return render_template('view_post.html', post=this_post, all_comment_content=all_comment_content, all_comments=all_comments)
    
@app.route('/add/comment/to/post', methods=['POST'])
def add_comment_to_post():
    comment.Comment.create_comment(request.form)
    id = request.form['post_id']
    return redirect(f'/post/{id}/comment')