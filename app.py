#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, make_response,redirect,render_template
import  json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return '<h1>hello cjj</h1>'

@app.route('/json')
def do_json():
    data = {"name":"chenjiajie","say":"hello"}
    return json.dumps(data)

@app.route('/status_500')
def status_500():
    return "hello",500

@app.route('/set_cookie')
def set_cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('username', 'evancss')
    return response

@app.route('/indexHello')
def indexhello():
    user = [{"username":u"陈佳杰","url":"/user/user1"},
            {"username": u"河滨", "url": "/user/user2"}]
    return render_template("index.html",title="user List",users = user)

if __name__ == '__main__':
    app.run()
