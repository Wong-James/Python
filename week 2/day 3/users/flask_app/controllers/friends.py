from flask_app import app
from flask import render_template, request, redirect, session, flash

from ..models.friend import Friend

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"],
    } 
    page = Friend.save(data)
    
    return redirect(f'/users/{page}')
    
    
@app.route('/update_friend', methods=["POST"])
def update_friend():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"],
        "id" : request.form["id"],
    } 
    page = Friend.update(data)
    
    return redirect('/')


@app.route('/create_a_friend')
def input_friend():
    return render_template("create.html")


@app.route('/users/<friends_id>')
def display_user(friends_id):
    display = Friend.display_friend({'id' : friends_id})
    return render_template("display_user.html", data=display)


@app.route('/users/<friends_id>/delete')
def delete_friend(friends_id):
    Friend.delete({'id': friends_id})
    return redirect("/")


@app.route('/users/<friends_id>/edit')
def edit_friend_form(friends_id):
    friends = Friend.display_friend({'id': friends_id})
    return render_template("edit_friend.html", friends = friends, friends_id = friends_id)