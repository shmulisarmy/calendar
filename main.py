from flask import Flask, request, session, redirect, render_template
from databaseInteraction import *
from datetime import datetime
import os
from utils import commonPassword, daysTool, sortedCalendarDates
from copy import deepcopy

app = Flask(__name__)
app.secret_key = bytes.fromhex('637065617365206b65792061206c656368616e676520636f6e74656e7420746f2073656372657420776f726b676572')

@app.route('/allEvents')
def index():
    userId = session.get('userId')
    if not userId:
        return redirect('/login')
    events = get_events_by_userId(userId)
    if not events:
        return send_message("you have no events")
    calendar = deepcopy(daysTool)
    for event in events:
        print(f"{event = }")
        day = event[2][-2:]
        if day not in calendar:
            calendar[day] = []
        calendar[day].append(event)
    print(f"{calendar = }")
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


@app.route('/updateEvent', methods=['POST', 'GET'])
def updateEvent():
    if request.method == 'GET':
        return render_template("updateEvent.html")
    userId = session.get('userId')
    print(f"updateEvent: {userId}")
    if userId == None:
        return send_message("you are not logged in")
    name = request.form['name']
    description = request.form['description']
    eventId = int(request.form['eventId'])
    if not name or not description:
        return send_message("name, description and date are all required")
    update_event(name, description, userId, eventId)
    return send_message(f"event updated successfully ({name = }{description = }{userId})")


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
    return send_message("you are now logged out")
    



@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    
    name = request.form['name']
    password = request.form['password']

    isCommon = commonPassword(password)
    if isCommon:
        return isCommon

    userId = create_user_if_not_exists(name, password)
    if not userId:
        return send_message("user already exists")
    session['userId'] = userId
    session['username'] = name
    return send_message("user create successfully" )


@app.route("/deleteEvent", methods=['POST'])
def deleteEvent():
    userId = session.get('userId')
    if userId == None:
        return "you are not logged in"
    print(f"{request.get_json() = }")
    eventId = request.get_json().get('eventId')
    print(f"deleteEvent: {userId = } {eventId = }")
    delete_event(userId, eventId)
    return "event deleted successfully"


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html", calendar=display_events())

def send_message(message):
    return render_template("base.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)