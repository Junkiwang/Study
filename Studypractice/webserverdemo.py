#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
from flask import Flask
from flask import request
import mysql.connector

app = Flask(__name__)
id = 1


@app.route('/', methods=['GET', 'POST'])
def home():
    return '''<h1><a href="http://localhost:5000/signin">Home</a></h1>'''


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
             <p><input name="username" placeholder="username"></p>
             <p><input name="password" placeholder="password" type="password"></p>
             <p><button type="submit">Sign in</button></p>
             </form>
             <a href="http://localhost:5000/signup"><button>Sign up</button></a>'''

@app.route('/signup', methods=['GET'])
def signup_form():
    return '''<form action="/signup" method="post">
             <p><input name="username" placeholder="username"></p>
             <p><input name="password" placeholder="password" type="password"></p>
             <p><button type="submit">Submit to Sign up</button></p>
                <a href="javascript:history.back(-1)">Back</a>
             </form>'''

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    if username == '' or password == '':
        return '''<h1>Invliad data!</h1>
               <a href="javascript:history.back(-1)">Back</a>'''
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    try:
        # 创建user表:
        cursor.execute(
            'create table if not exists user (id varchar(20) primary key, name varchar(20), password varchar(20))')
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute('insert into user (id, name, password) values (%s, %s, %s)', (id, username, password))
        # 提交事务:
        conn.commit()
    except Exception as msg:
        print(msg)
        return '''<h3>数据存储错误！</h3>
                <a href="javascript:history.back(-1)">Back</a>'''
    finally:
        cursor.close()
        conn.close()
        global id
        id += 1
        return '''<h3>Sign up Success!</h3>
                <a href="javascript:history.back(-1)">Back to sign in</a>'''


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()

    if username == '' or password == '':
        return '''<h1>Invliad data!</h1>
                <a href="javascript:history.back(-1)">Back</a>'''
    try:
        cursor.execute('select name from user')
        result1 = cursor.fetchall()
        cursor.execute('select * from user where name = %s', (username,))
        result2 = cursor.fetchall()
    except Exception as msg:
        print(msg)
        return '''<h3>用户不存在！</h3>
                <a href="javascript:history.back(-1)">Back to sign in</a>'''
    finally:
        cursor.close()
        conn.close()
    for name in result1:
        if username == name[0]:
            if result2[0][2] == password:
                return '<h3>Hello, Welcome!</h3>'
            else:
                return '<h3>Wrong username or password.</h3>'
    return '''<h3>Invalid user！</h3>
             <a href="javascript:history.back(-1)">Back to sign in</a>'''


if __name__ == '__main__':
    app.run()
