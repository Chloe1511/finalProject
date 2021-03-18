from datetime import timedelta
from flask import Flask, redirect, render_template
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask import request, session


app = Flask(__name__)
api = Api(app)
app.secret_key = '123'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/instructions', methods=['GET', 'POST'])
def instructions():
    id = ''
    if 'code' in request.args:
        id = request.args['code']
    return render_template('instructions.html', id=id)


@app.route('/consent')
def consent():
    return render_template("consent.html")


@app.route('/PreTest')
def pretest():
    return render_template("PreTest.html")


@app.route('/video1')
def video1():
    return render_template("video1.html")


@app.route('/video2')
def video2():
    return render_template("video2.html")


@app.route('/afterTest')
def afterTest():
    return render_template("afterTest.html")


@app.route('/demog')
def demog():
    return render_template("demog.html")


@app.route('/request')
def request():
    return render_template("end.html")


@app.route('/end')
def end():
    return render_template("end.html")


@app.route('/timer')
def timer():
    return render_template("Timer.html")


if __name__ == '__main__':
    app.run()
