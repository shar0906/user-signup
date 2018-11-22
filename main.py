#!/usr/bin/env python3
from flask import Flask, render_template, redirect, url_for, request
import logging
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        counter = 0
        messages = {}

        if validate(request.form['username']) == False:
            counter += 1
            messages['message1'] = "Your username is invalid!"

        if validate(request.form['password']) == False:
            counter += 1
            messages['message2'] = "Your password is invalid!"
        
        verify = request.form['verify']
        if verify != request.form['password']:
            counter += 1
            messages['message3'] = "Your passwords must match!"
        
        email = request.form['email']
        if email:
            if not '@' in email or not '.' in email:
                counter += 1
                messages['message4'] = "Please enter a valid email address!"

        if counter == 0:
            return "<h1>Hey man good job!</h1>"
        else:
            return redirect(url_for('index', **messages, **request.form))

def validate(value):
    if value:
        if ' ' in value:
            return False
        if 3 > len(value) or len(value) > 20: 
            return False
    else:
        return False

app.run(debug = True)
