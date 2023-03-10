import sqlite3
import json
from models import Moods

def get_all_moods():
    # Open a connection to the database
    with sqlite3.connect("./journal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM Moods m
        """)

        # Initialize an empty list to hold all mood representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a mood instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Moods class above.
            mood = Moods(row['id'], row['label'])

            moods.append(mood.__dict__)

    return moods

def get_single_mood(id):
    """docstring"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m. label
        
        FROM Moods m
        WHERE m.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Moods(data['id'], data['label'])

    return entry.__dict__