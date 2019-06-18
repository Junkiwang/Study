#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
from flask import Flask
from flask import render_template
from flask import request
from flask import *
import mysql.connector

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin_form', methods=['GET'])
def signin_form():
    return render_template('signin_form.html')


@app.route('/signup_form', methods=['GET'])
def signup_form():
    return render_template('signup_form.html')


@app.route('/signup_form', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    if username == '' or password == '':
        return render_template('signup_form.html', message="Invliad data!", username=username)
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    try:
        # 创建user表:
        cursor.execute(
            'create table if not exists user (id varchar(20) primary key, name varchar(20), password varchar(20))')
        # 判断用户名是否已被注册
        cursor.execute('select name from user')
        namelist = cursor.fetchall()
        for x in namelist:
            if username == x[0]:
                return render_template('signup_form.html',
                                       message="This username had been registered,please use another name!",
                                       username=username)
        # 判断表中id序号
        cursor.execute('select id from user')
        idlist = cursor.fetchall()
        if idlist == []:
            id = 1
        else:
            id = int(max(idlist)[0]) + 1
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute('insert into user (id, name, password) values (%s, %s, %s)', (id, username, password))
        # 提交事务:
        conn.commit()
        return render_template('signup_ok.html')
    except Exception as msg:
        print(msg)
        return render_template('signup_form.html', message="数据存储错误!", username=username)
    finally:
        cursor.close()
        conn.close()


@app.route('/signin_form', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connector.connect(user='root', password='password', database='test')
    cursor = conn.cursor()

    if username == '' or password == '':
        return render_template('signin_form.html', message="Invliad data!", username=username)
    try:
        cursor.execute('select name from user')
        result1 = cursor.fetchall()
        cursor.execute('select * from user where name = %s', (username,))
        result2 = cursor.fetchall()
    except Exception as msg:
        print(msg)
        return render_template('signin_form.html', message="用户不存在!", username=username)
    finally:
        cursor.close()
        conn.close()
    for name in result1:
        if username == name[0]:
            if result2[0][2] == password:
                return render_template('signin_ok.html', username=username)
            else:
                return render_template('signin_form.html', message="Wrong username or password!", username=username)
    return render_template('signin_form.html', message="Invalid user!", username=username)


if __name__ == '__main__':
    app.run(host='172.18.20.165')
