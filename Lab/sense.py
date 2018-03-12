import os
import json
from flask import Flask, render_template, g, request, redirect, jsonify
from sqlite3 import dbapi2 as sqlite3
app = Flask(__name__)

##### APP SETUP #####
app = Flask(__name__)

##### DB SETUP #####

# Setup the database credentials
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'sensor.db'),
    DEBUG=True,
    SECRET_KEY=b'<SOME HEXADECIMAL SECRET KEY>',
    USERNAME='admin',
    PASSWORD='<SOME PASSWORD>'
))

# Connect to the DB
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Wrap the helper function so we only open the DB once
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Create the database (we do this via command line!!!)
def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('data.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# Command to create the database via command line
# You call it from command line: flask initdb
@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

# Close the database when the request ends
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


#db.close()
@app.route('/')
def dash():
    db = get_db()
    cur = db.execute('SELECT * FROM data')
    dataSQL = cur.fetchall()

    data_as_dict = []
    for entry in dataSQL:
        data_as_dict_sing = {
            'envelope' : entry[0],
            'humidity' : round(entry[1],1),
            'light' : entry[2],
            'tempC' : round(entry[3],1),
            'tempF' : round(entry[4],1)
        }
        data_as_dict.append(data_as_dict_sing)  
    dataJSON = json.dumps(data_as_dict)
    with open('static/data.json','w') as f:
            f.write(dataJSON)
    return render_template('dashboard.html')

@app.route('/temperature')
def temp():
    db = get_db()
    count_id=request.args.get('count')
    j=int(count_id)
    cur = db.execute('SELECT temp_c, temp_f FROM data')
    dataSQL = cur.fetchall()
    data_as_dict = []
    i=0
    for entry in dataSQL:
        if i >= 60-j:
            data_as_dict_sing = {
                'tempC' : round(entry[0],1),
                'tempF' : round(entry[1],1)
            }
            data_as_dict.append(data_as_dict_sing)
        i += 1
    return jsonify(data_as_dict)
@app.route('/light')
def light():
    db = get_db()
    count_id=request.args.get('count')
    j=int(count_id)
    cur = db.execute('SELECT light FROM data')
    dataSQL = cur.fetchall()
    data_as_dict = []
    i=0
    for entry in dataSQL:
        if i >= 60-j:
            data_as_dict_sing = {
                'light' : round(entry[0],1),
            }
            data_as_dict.append(data_as_dict_sing)
        i += 1
    return jsonify(data_as_dict)
@app.route('/sound')
def sound():
    db = get_db()
    count_id=request.args.get('count')
    j=int(count_id)
    cur = db.execute('SELECT envelope FROM data')
    dataSQL = cur.fetchall()
    count=request.args.get('count')
    data_as_dict = []
    i=0
    for entry in dataSQL:
        if i >= 60-j:
            data_as_dict_sing = {
                'sound' : round(entry[0],1),
            }
            data_as_dict.append(data_as_dict_sing)
        i += 1
    return jsonify(data_as_dict)
@app.route('/humidity')
def humid():
    db = get_db()
    count_id=request.args.get('count')
    j=int(count_id)
    cur = db.execute('SELECT humidity FROM data')
    dataSQL = cur.fetchall()
    data_as_dict = []
    i=0
    for entry in dataSQL:
        if i >= 60-j:
            data_as_dict_sing = {
                'humidity' : round(entry[0],1),
            }
            data_as_dict.append(data_as_dict_sing)
        i += 1
    return jsonify(data_as_dict)


