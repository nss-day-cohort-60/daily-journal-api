import sqlite3
def update_user(id, new_user):
    """hi sydney<3"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Users
            SET
                name = ?,
                email = ?
        WHERE id = ?
        """, (new_user['name'], new_user['email'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
