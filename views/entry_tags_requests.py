import json
import sqlite3
from models import Entries, EntryTags, Tags

def get_all_entry_tags():
    """docstring"""
    # Open a connection to the database
    with sqlite3.connect("./journal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.timestamp,
            e.concepts,
            e.journal_entry,
            e.user_id,
            e.mood_id,
            et.id,
            et.entry_id,
            et.tag_id,
            t.id,
            t.subject
        FROM Entry_tags et
        JOIN entries e
            ON e.id = et.entry_id
        JOIN Tags t 
            ON t.id = et.tag_id
        """)

        # Initialize an empty list to hold all animal representations
        entry_tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

    # Create an animal instance from the current row
            entry = Entries(row['id'], row['timestamp'],
            row['concepts'], row['journal_entry'], row['user_id'],
            row['mood_id'])

            del entry.id

            entry_tag = EntryTags(row['id'], row['entry_id'], row['tag_id'])

            tag = Tags(row['id'], row['subject'])

            del tag.id

            entry_tag.entry = entry.__dict__
            entry_tag.tag = tag.__dict__

            entry_tags.append(entry_tag.__dict__)

    return entry_tags

def delete_entry_tag_with_entryid(entry_id):
    """this is to delete individual entry using SQL"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Entry_Tags
        WHERE id = ?
        """, (entry_id, ))
        
