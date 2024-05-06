from fastapi import FastAPI, File, UploadFile, Query, Form, Response, status, Request, Path, APIRouter
import sqlite3
import hashlib
import os
from fastapi.templating import Jinja2Templates




users_router = APIRouter(prefix="/users", tags=["users"])
templates = Jinja2Templates(directory="templates")


@users_router.post("/signup")
def signup(response: Response, username: str = Form(...), password: str = Form(...), email: str = Form(...)):


    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    if c.execute("SELECT * FROM users WHERE name = ?", (username,)).fetchone() is not None:
        return {"message": "this user already exists"}
    
    salt = hashlib.sha256(os.urandom(32)).hexdigest()
    hashed_password_with_salt = hashlib.sha256(f"{password}{salt}".encode("utf-8")).hexdigest()
    c.execute("INSERT INTO users(name, password, email, salt) values(?,?,?,?)", (username, hashed_password_with_salt, email, salt))
    conn.commit()
    conn.close()

    response.set_cookie(key="session_token", value=username)
    return {"message": "user created"}



@users_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="session_token")
    return {"message": "Logout successful"}

@users_router.post("/login")
async def login(response: Response, username: str, password: str):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("SELECT salt, password FROM users WHERE name = ?", (username,))

    last_row = c.fetchone()
    print(f"last row: {last_row}")
    if not last_row:
        print(f"user {username} does not exist")
        return {"message": "this user does not exist"}
        
    salt, db_password = last_row

    hashed_password_with_salt = hashlib.sha256(f"{password}{salt}".encode("utf-8")).hexdigest()
    print(f"hashed_password_with_salt: {hashed_password_with_salt}, db_password: {db_password}")
    if hashed_password_with_salt != db_password:
        print(f"invalid password for user {username}")
        return {"message": "Invalid username or password"}

    response.set_cookie(key="session_token", value=username)
    return {"message": "Login successful"}


@users_router.post("/create")
def create_user(name: str = Form(...), password: str = Form(...), email: str = Form(...)):
    conn = sqlite3.connect("main.db")
    c = conn.cursor()
    c.execute("INSERT INTO users(name, password, email) values(?,?,?)", (name, password, email))
    conn.commit()
    conn.close()
    return Response(status_code=status.HTTP_201_CREATED)

