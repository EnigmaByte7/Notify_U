from flask import Flask, render_template, request
import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)
"""
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

@app.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        contact = request.form.get('contact')
        con = sqlite3.connect('database.db')
        cursor = con.cursor()
        cursor.execute("Insert into users (name,contact) values(?,?)",(name, contact))
        con.commit()
        print("Success")
        return "Success"
    else:
        return render_template('index.html')
  """
dt = datetime.datetime.now()
date = dt.strftime("%d/%m/%Y")
result=[]

def notifier(notices):
     pass

def updater(result,date):
    notices = []
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    for i in result:
         data = cursor.execute("select notice from notices where date=(?) and notice=(?)",(date,i))
         if data == []:
              notices.append(i)
              cursor.execute("insert into notices values(?,?)",(date,i))
    notifier(notices)

def extractor(date):
        with open("jec.html") as page:
            soup = BeautifulSoup(page, "html.parser")
            obj = soup.find(id = 'ctl00_ContentPlaceHolder1_WC_MoreUtility1_GVView')
            tables = obj.find_all('table')
            for i in range(1, len(tables)):
                main = tables[i].find_all('td')
                if main[1].get_text(strip=True) == date:
                        result.append(main[2].get_text(strip=True))
                        print(main[2].get_text(strip=True))
                else:
                    break
        if result != []:
            updater(result)