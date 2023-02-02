import json
import sqlite3

def delete_entry_tag_with_entryid(entry_id):
    """this is to delete individual entry using SQL"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Entry_Tags
        WHERE id = ?
        """, (entry_id, ))