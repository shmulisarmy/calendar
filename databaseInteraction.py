from sqlite3 import connect



def create_user_if_not_exists(name, password) -> bool|int:
    conn = connect("database.db")
    """Create a new user in the database."""
    cursor = conn.execute("SELECT id FROM users WHERE name = ?", (name,))
    if cursor.fetchone():
        return False
    conn.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    cursor = conn.execute("SELECT id FROM users WHERE name = ?", (name,))
    userId = cursor.fetchone()[0]
    conn.commit()
    return userId


def returns_name_and_id_if_user_exists_and_password_is_correct(name, password) -> tuple["userId", "username"]|None:
    conn = connect("database.db")
    """to be used when user is logging in and in order to check if password is correct and if so get id"""
    cursor = conn.execute("SELECT id, name FROM users WHERE name = ? AND password = ?", (name, password))
    row = cursor.fetchone()
    if row:
        return row
    return None

def create_event(name: str, description: str, date: str, user_id) -> None:
    conn = connect("database.db")
    """Create a new event in the database."""
    conn.execute("INSERT INTO events (name, description, date, user_id) VALUES (?, ?, ?, ?)", (name, description, date, user_id))
    conn.commit()

def get_events_by_userId(userId):
    conn = connect("database.db")
    """Retrieve events from the database using a username."""
    # First, get the user_id for the given username
    cursor = conn.execute("SELECT name, description, date FROM events WHERE user_id = ?", (userId,))
    events = cursor.fetchall()

    return events


def display_events():
    conn = connect("database.db")
    """Retrieve events from the database."""
    cursor = conn.execute("SELECT name, description, date, user_id FROM events")
    events = cursor.fetchall()
    return events


