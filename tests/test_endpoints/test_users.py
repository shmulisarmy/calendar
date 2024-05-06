import requests
from settings import *


this_url = url+"/users"


def test_login():
    """makes sure that the login route wont allow access to a non-existing user"""
    data = {
        "username": "non-existing-user",
        "password": "anything",
    }
    
    assert requests.post(f"{this_url}/login", data=data).json() == {"message": "this user does not exist"}


def test_signup():
    """makes sure that the signup route wont allow creation of an existing user"""
    data = {
        "username": "Shmuli",
        "password": "test_password",
        "email": "test_email",
    }
    
    assert requests.post(f"{this_url}/signup", data=data).json() == {"message": "this user already exists"}