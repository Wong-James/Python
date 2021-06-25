from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "whack"

@app.route('/')
def counter():
    if 'visit' in session:
        print('key exists!')
        session['visit'] += 1
    else:
        session['visit'] = 1
        print("key 'key_name' does NOT exist")
    return render_template('index.html', increment = session['visit'])
# dd = {
#     'key' : value
# }

# dd['key'] = value
@app.route('/add_visit', methods = ['POST'])
def add_button():
    session['visit'] += 1

    return redirect('/')

@app.route('/add_visit2')
def addition():
    session['visit'] += 1
    return redirect('/')



@app.route('/destroy_session')
def reset():
    session.clear()

    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)

