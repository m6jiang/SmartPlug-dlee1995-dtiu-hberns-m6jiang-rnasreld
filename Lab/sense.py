import os
from flask import Flask, render_template, g, request, redirect
from sqlite3 import dbapi2 as sqlite3
app = Flask(__name__)

#def get_tempcel(temp):
#       return celsius
#def get_tempfah(temp):
#       return fahrenheit
#def get_humdity(hum):
#       return humidity
#def get_audio(sound):
#       return gate, envelope, audio

db = sqlite3.connect('lab_4.db')

#db.create("get_cel", 1, get_tempcel)
#db.create("get_fah", 1, get_tempfah)
#db.create("get_hum", 1, get_humdity)
#db.create("get_sound", 1, get_audio)

c = db.cursor()
c.execute('''DROP TABLE IF EXISTS temperature''')
c.execute('''CREATE TABLE temperature (id INTEGER PRIMARY KEY autoincrement, fahrenheit INTEGER, celsius INTEGER);''')
#c.execute('''CREATE TABLE humidity (humidity text)''')
#c.execute('''CREATE TABLE sound (audio text, envelope text, gate text)''')
c.execute('''INSERT INTO temperature (fahrenheit, celsius) VALUES (72, 22.2), (75, 23.9), (91, 32.8), (87, 30.6);''')
#c.execute('''INSERT INTO temperature VALUES (75, 23.9)''')
#c.execute('''INSERT INTO temperature VALUES (91, 32.8)''')
#c.execute('''INSERT INTO temperature VALUES (87, 30.6)''')
#c.execute('''INSERT INTO humidity VALUES (get_humidity)''')
#c.execute('''INSERT INTO audio VALUES (get_audio)''')
db.commit()

#db.close()
@app.route('/')
def dash():
    return render_template('dashboard.html')

@app.route('/temperature', methods=['GET'])
def Layout():
    db = sqlite3.connect('lab_4.db')
    id=request.args.get('id')
    if id=='Temperature':
        pr = db.execute('''SELECT fahrenheit, celsius FROM temperature''')
        data = pr.fetchall()
        print(data)
        return render_template('getTable.html', pr2=data)
