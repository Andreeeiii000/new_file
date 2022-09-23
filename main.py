from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("sityes.html")

@app.route('/lybrary')
def sityes():
    return render_template("index.html")


@app.route('/<name>')
def print_name(name):
    return f"<h1>Hello {name} </h1>"

app.run(debug=True)