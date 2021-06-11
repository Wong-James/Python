from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def form_submit():
    print(request.form["name"])
    print(request.form['location'])
    print(request.form['language'])
    print(request.form['comment'])
    return render_template(
        'index2.html',
        name = request.form['name'], 
        location = request.form['location'],
        language = request.form['language'],
        comment = request.form['comment'])

if __name__=="__main__":
    app.run(debug = True)