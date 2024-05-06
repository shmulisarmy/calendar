from fastapi import FastAPI, File, UploadFile, Query, Form, Response, status, Request, Path
from fastapi import FastAPI, Request, Response, HTTPException, Depends, Cookie
from fastapi.templating import Jinja2Templates
from typing import Optional
import sqlite3
from logic.availiblity import get_availabilies, get_availabilies_together

from users import users_router



app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(users_router)






def authenticate_user(session_token: Optional[str] = Cookie(None)):
    if session_token is None:
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            detail="you are not allowed to see this page",
        )
    # Here you might validate the session token against your database or cache
    # and retrieve user information if the session is valid
    return session_token

@app.get("/protected")
async def protected_route(user: str = Depends(authenticate_user)):
    return {"data": "secret stuff", "user": user}


@app.get("/")
def index(request: Request, username: str = Depends(authenticate_user)):
    return templates.TemplateResponse("calendar.html", {"request": request, "username": username})

@app.get("/shared_availability/{other_user_id}/{date}")
def get_availabilies_together_view(
    other_user_id: int, date: str,
    request: Request,
    username: str = Depends(authenticate_user)
):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users where name = ?", (username,))
    this_user_id = c.fetchone()[0]
    conn.close()

    shared_availabilities = get_availabilies_together(this_user_id, other_user_id, date)

    return templates.TemplateResponse("shared_availability.html", {"request": request, "shared_availabilities": shared_availabilities})




@app.get("/all_users")
def get_users(reqest: Request):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("SELECT name, email, id FROM users")
    users: list = c.fetchall()
    conn.close()

    today = "2020-01-01"
    availabilities = []

    for user in users:
        availabilities.append(get_availabilies(user[2], today))
        print(f"availabilities: {availabilities}")

    return templates.TemplateResponse("users.html", {"request": reqest, "users": users, "availabilities": availabilities, "get_availabilies": get_availabilies, "today": today})


@app.get("/events")
def get_user_events(request: Request, username: str = Depends(authenticate_user)):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("SELECT * FROM events where user_id = (select id from users where name = ?)", (username,))
    events = c.fetchall()
    conn.close()
    return templates.TemplateResponse("events.html", {"request": request, "events": events})



# @app.get("/events/{user_id}")
# def get_events_by_user_id(request: Request, username: str = Depends(authenticate_user)):
#     conn = sqlite3.connect("main.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM events where user_id = (select id from users where name = ?)", (username,))
#     events = c.fetchall()
#     conn.close()
#     return templates.TemplateResponse("events.html", {"request": request, "events": events})


@app.get("/events/date/{date}")
def get_events_by_date(request: Request, date: str, username: str = Depends(authenticate_user)):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("SELECT * FROM events where date = ? and user_id = (select id from users where name = ?)", (date, username))
    events = c.fetchall()
    conn.close()
    return templates.TemplateResponse("events.html", {"request": request, "events": events, "date": date})



@app.get("/events/date/{date}")
def get_events_by_date(request: Request, date: str, username: str = Depends(authenticate_user)):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("SELECT * FROM events where date = ?  and user_id = (select id from users where name = ?)", (date, username))
    events = c.fetchall()
    conn.close()
    return templates.TemplateResponse("events.html", {"request": request, "events": events})



@app.post("/events/create")
def create_event(name: str = Form(...), username: str = Depends(authenticate_user), description: str = Form(...), date: str = Form(...)):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("INSERT INTO events(name, user_id, description, date) values(?,(select id from users where name = ?),?,?)", (name, username, description, date))
    conn.commit()
    conn.close()
    return {"message": "Event created"}



@app.get("/event/{id}")
def get_event_by_id(request: Request, id: int, username: str = Depends(authenticate_user)):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("SELECT id, name, description, date FROM events where id = ? and user_id = (select id from users where name = ?)", (id, username))
    last_row = c.fetchone()
    if not last_row:
        return {"message": "this event does not exist or does not belong to you"}
    print(f"{last_row = }")
    id, name, description, date = last_row
    conn.close()
    return templates.TemplateResponse("event.html", {"request": request, "id": id, "name": name, "description": description, "date": date})






@app.post("/events/delete")
def delete_event(id: int = Form(...), username: str = Depends(authenticate_user)):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("DELETE FROM events where id = ? and user_id = (select id from users where name = ?)", (id, username))
    conn.commit()
    conn.close()
    return {"message": "succes"}



@app.post("/events/edit_text/{id}")
def edit_event(id: int, name: str = Form(...), description: str = Form(...), username: str = Depends(authenticate_user)):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("UPDATE events set name = ?, description = ? where id = ? and user_id = (select id from users where name = ?)", (name, description, id, username))
    conn.commit()
    c.execute("SELECT * FROM events where id = ?", (id,))
    event = c.fetchone()
    conn.close()
    return event
    

