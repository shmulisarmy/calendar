import requests
import pytest

from settings import *





def test_protected():
    """makes sure that the protected route is protected"""
    assert requests.get("http://127.0.0.1:8000/protected").text == '{"detail":"you are not allowed to see this page"}'


def test_events():
    """makes sure that the events route is protected"""
    print(requests.get(f"{url}/events").json())
    assert requests.get(f"{url}/events").json() == {"detail":"you are not allowed to see this page"}

