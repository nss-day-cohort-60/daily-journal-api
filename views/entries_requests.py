import json
import sqlite3
from models import Entries

def delete_entry(id):
    """this is to delete individual entry using SQL"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Entries
        WHERE id = ?
        """, (id, ))

def get_all_entries():
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
            e.mood_id
            
        FROM Entries e
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

    # Create an animal instance from the current row
            entry = Entries(row['id'], row['timestamp'],
            row['concepts'], row['journal_entry'], row['user_id'],
            row['mood_id'])

            entries.append(entry.__dict__)

    return entries

def get_single_entry(id):
    """docstring"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.timestamp,
            e.concepts,
            e.journal_entry,
            e.user_id,
            e.mood_id
        FROM Entries e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entries(data['id'], data['timestamp'], data['concepts'], data['journal_entry'], data['user_id'], data['mood_id'])

    return entry.__dict__



def search_journal_entries(search_term):
    """docstring"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        query = """SELECT * FROM entries WHERE journal_entry LIKE ?"""

        db_cursor.execute (query, ('%' + search_term + '%',))
        entries=[]
        data = db_cursor.fetchall()
        for row in data:
            entry = Entries(row['id'], row['timestamp'], row['concepts'], row['journal_entry'], row['user_id'], row['mood_id'])
            entries.append(entry.__dict__)

    return entries
def update_entry(id, new_entry):
    """hi sydney<3"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entries
            SET
                timestamp = ?,
                concepts = ?,
                journal_entry = ?,
                user_id = ?,
                mood_id = ?
        WHERE id = ?
        """, (new_entry['timestamp'], new_entry['concepts'], new_entry['journal_entry'], new_entry['user_id'], new_entry['mood_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
