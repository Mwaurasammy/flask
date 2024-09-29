from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('child.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

