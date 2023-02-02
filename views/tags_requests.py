import sqlite3
import json
from models import Tags

def create_tag(new_tag):
    """ creates a new tag and adds it to the database """
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags 
            (subject)
        VALUES
            (?)
        """, (new_tag['subject'], ))

        id = db_cursor.lastrowid
        new_tag['id'] = id
    return new_tag