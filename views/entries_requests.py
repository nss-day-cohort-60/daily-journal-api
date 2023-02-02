def create_entry(new_entry):
    """Returns new dictionary with id property added"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entries
            ( timestamp, concepts, journal_entry, user_id, mood_id)
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_entry['timestamp'], new_entry['concepts'], new_entry['journal_entry'], new_entry['user_id'], new_entry['mood_id']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id

    return new_entry