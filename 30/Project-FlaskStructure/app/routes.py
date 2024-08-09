# app/routes.py
from flask import render_template
from app import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'About Page'
