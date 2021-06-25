import re
from flask_app.models.user import User
from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/register/user', methods=['POST'])
def register():
    print(request.form)
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect("/success")


@app.route('/login', methods=['POST'])
def login():
    if not User.login_validator(request.form):
        return redirect('/')

    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    session['user_id'] = user_in_db.id
    return redirect("/success")

@app.route('/success')
def login_page():
    user = User.get_one({'id': session['user_id']})
    return render_template('success.html', user = user)

@app.route('/logout')
def logout():
    session['user_id'] = 0
    print(session['user_id'])
    return redirect('/')