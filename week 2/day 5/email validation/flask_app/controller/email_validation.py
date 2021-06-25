from flask_app.model.user import User
from flask_app import app
from flask import redirect, request, render_template, session, flash


@app.route("/")
def input():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    User.create(request.form)
    print(request.form)
    return redirect('/dashboard')

@app.route('/dashboard')
def success():
    emails = User.display_user()
    print(emails)
    return render_template('success.html', emails = emails)
