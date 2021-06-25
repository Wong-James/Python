from flask_app.models.ninja import Ninja
from flask_app import app
from flask import render_template, redirect, request, session, flash
from ..models.dojo import Dojo

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.display_dojos()
    print(dojos)
    return render_template('index.html', dojos = dojos)

@app.route('/dojos/create', methods = ['POST'])
def create_dojo():
    print(request.form)
    Dojo.create(request.form)

    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):

    return render_template("dojo_show.html", display = Dojo.dojo_ninjas({'id': dojo_id}))


@app.route('/ninjas/new')
def new_ninja():
    dojos = Dojo.display_dojos()
    return render_template('create_ninja.html', dojos = dojos)

@app.route('/ninja/add_ninja', methods = ['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    dojoid = request.form["dojo_id"]
    print(dojoid)
    return redirect(f'/dojos/{dojoid}')