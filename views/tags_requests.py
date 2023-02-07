import sqlite3
import json
from models import Tags


def get_all_tags():
    
    with sqlite3.connect("./journal.sqlite3") as conn:

        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            t.id,
            t.subject
        FROM Tags t
        """)

        
        tags = []

        
        dataset = db_cursor.fetchall()

        
        for row in dataset:

            tag = Tags(row['id'], row['subject'])

            tags.append(tag.__dict__)

    return tags

def get_single_tag(id):
    """docstring"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


        db_cursor.execute("""
        SELECT
            t.id,
            t.subject
        
        FROM Tags t
        WHERE t.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Tags(data['id'], data['subject'])

    return entry.__dict__