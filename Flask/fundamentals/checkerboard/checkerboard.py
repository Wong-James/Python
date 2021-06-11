from flask import Flask, render_template 
app = Flask(__name__)


@app.route('/')
def main_board():
    return render_template('index.html', height = 8, width = 8)

@app.route('/<int:x>')
def row_board(x):
    return render_template('index.html', height = 8, width = x)

@app.route('/<int:x>/<int:y>')
def row_col(x, y):
    return render_template('index.html', height = y, width = x)


if __name__=="__main__":       
    app.run(debug=True) 