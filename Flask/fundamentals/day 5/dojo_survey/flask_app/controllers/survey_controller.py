from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.survey_info import Survey_info


@app.route('/')
def form():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def form_submit():
    if not Survey_info.validate_info(request.form):
        return redirect('/')
    return render_template(
        'index2.html',
        name = request.form['name'], 
        location = request.form['location'],
        language = request.form['language'],
        comment = request.form['comment'])
