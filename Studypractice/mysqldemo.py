#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:
# coding:utf-8

from idna import unicode
import requests
from bs4 import BeautifulSoup
import lxml
import json
import mysql.connector

id = 0


# 获取网页返回信息
def get_response(page):
    resp = requests.get('http://book.douban.com/top250', params={'start': str(page * 25)})
    if resp.status_code == 200:
        return resp.text
    else:
        raise RecursionError('fail to request to target.')

#使用BeautifulSoup解析
def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find('div', id='wrapper').find_all('table')
    for table in tables:
        img = table.find('img')['src']
        name = table.select('.pl2')[0].a['title']
        string = unicode(table.find('p').string)
        lst = string.split('/')
        author = lst[0].strip()
        publisher = lst[-3].strip()
        date = lst[-2].strip()
        price = lst[-1].strip()
        credit = unicode(table.select('.rating_nums')[0].string)
        try:
            desc = unicode(table.select('.inq')[0].string)
        except IndexError:
            desc = '无'
        global id
        id += 1
        yield{'id': id, 'img': img, 'name': name, 'author': author, 'publisher': publisher,
              'date': date, 'price': price, 'credit': float(credit), 'desc': desc}

#写入文件
def write_to_file():
    with open('book.txt', 'w') as f:
        for i in range(10):
            for book in parse_html(get_response(i)):
                json.dump(book, f, ensure_ascii=False)
                f.wirte('\n')
                print(book, 'was saved into book.txt')

#存入数据库
def save():
    for i in range(10):
        for book in parse_html(get_response(i)):
            save_to_db(book['id'], book['img'], book['name'], book['author'], book['publisher'], book['date'], book['price'],
                       book['credit'], book['desc'])
            print('save book' + str(book) + 'to db')

#存入一本书到数据库
def save_to_db(*args):
    try:
        conn = mysql.connector.connect(user='root', password='password', database='test', charset='utf8')
        cursor = conn.cursor()
        cursor.execute('create table if not exists book(id int(11) primary key, img varchar(100), name varchar(30), '
                       'author varchar(30), publisher varchar(30), date varchar(20), price varchar(10), '
                       'credit float,  description varchar(30))')
        cursor.execute('insert into book(id, img, name, author, publisher, date, price, credit, description)'
                       ' values(%s, %s, %s, %s, %s, %s, %s, %s, %s)', args)
        conn.commit()
    except Exception as e:
        print('出错', e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    save()
# import mysql.connector
#
# # change root password to yours:
# conn = mysql.connector.connect(user='root', password='password', database='test', charset='utf8')
#
# cursor = conn.cursor()
# # 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
# print('rowcount =', cursor.rowcount)
# # 提交事务:
# conn.commit()
# cursor.close()
#
# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# # 关闭Cursor和Connection:
# cursor.close()
# conn.close()