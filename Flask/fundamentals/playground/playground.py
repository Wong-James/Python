from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "This is the Homepage!"


@app.route('/play')
def play():
    return render_template('index.html', times = 3, color = "black")

@app.route('/play/<int:id>')
def play_count(id):
    return render_template('index.html', times = id, color = "black")

@app.route('/play/<int:id>/<color>')
def play_color(id, color):
    return render_template('index.html', times = id, color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 
