from flask import Flask, render_template, request
import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime
from twilio.rest import Client
import schedule
import time

app = Flask(__name__)

con = sqlite3.connect('database.db')
cursor = con.cursor()
table1 = '''create table IF NOT EXISTS users(name TEXT NOT NULL, contact INTEGER NOT NULL)'''
cursor.execute(table1)
con.commit()
table2 = '''create table IF NOT EXISTS notices(notice_date DATE, notice TEXT)'''
cursor.execute(table2)
con.commit()
@app.route("/")
def index():
    return render_template('index.html')

sid = 'SK23177b5091136a79b677e071d4414eb6'
secret = 'DTEXPp7P5lFpqkJwlJMb8Lkxuu6rzwIN'

@app.route("/register", methods=['POST']) 
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        contact = request.form.get('contact')
        con = sqlite3.connect('database.db')
        cursor = con.cursor()
        cursor.execute("Insert into users values(?, ?)",(name,contact))
        con.commit()
        return "Success"
    else:
        return render_template('index.html')

app.run()


