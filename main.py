from flask import Flask, request, session, redirect, render_template
from databaseInteraction import *
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/allEvents')
def index():
    userId = session.get('userId')
    if not userId:
        return redirect('/login')
    events = get_events_by_userId(userId)
    if not events:
        return "you have no events"
    calendar = {}
    for event in events:
        if event[2] not in calendar:
            calendar[event[2]] = []
        calendar[event[2]].append(event)
    sortedCalendarDates = sorted(calendar.keys())
    return render_template("index.html", calendar=calendar, sortedCalendarDates=sortedCalendarDates, name=session.get('username'))



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    name = request.form['name']
    password = request.form['password']
    rv = returns_name_and_id_if_user_exists_and_password_is_correct(name, password)
    if rv is None:
        return send_message("user not found or password incorrect")
    print(f"{rv = }")
    session['userId'] = rv[0] 
    session['username'] = rv[1] 
    return send_message("user logged in successfully")


@app.route('/createEvent', methods=['POST', 'GET'])
def createEvent():
    if request.method == 'GET':
        return render_template("createEvent.html")
    userId = session.get('userId')
    print(f"createEvent: {userId}")
    if userId == None:
        return send_message("you are not logged in")
    name = request.form['name']
    description = request.form['description']
    date = request.form['date']
    if not name or not description or not date:
        return send_message("name, description and date are all required")
    create_event(name, description, date, userId)
    return send_message(f"event created successfully ({name = }{description = }{date = }{userId})")


@app.route('/getEvents', methods=['GET'])  
def getEvents():
    userId = session.get('userId')
    if userId == None:
        return redirect('/login')
    events = get_events_by_userId(userId)

    if events is None:
        return send_message("you have no events")
    
    days = {}
    for event in events:
        if event[2] not in days:
            days[event[2]] = []
        days[event[2]].append(event)

    return events


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    



@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    
    name = request.form['name']
    password = request.form['password']

    userId = create_user_if_not_exists(name, password)
    if not userId:
        return send_message("user already exists")
    session['userId'] = userId
    session['username'] = name
    return send_message("user create successfully" )


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html", calendar=display_events())

def send_message(message):
    return render_template("base.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)