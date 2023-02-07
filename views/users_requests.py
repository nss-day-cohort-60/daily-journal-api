import sqlite3
from models import Users
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

def create_user(new_user):
    """ sydney's here? hi sydney! """
    with sqlite3.connect("./journal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Users
            (name, email)
        VALUES
            (?, ?)
        """, (new_user['name'],new_user['email'],))

        id = db_cursor.lastrowid
        new_user['id'] = id
    return new_user
    
def get_all_users():
    """ sydney's here? hi sydney! """
    with sqlite3.connect("./journal.sqlite3") as conn:

        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        
        db_cursor.execute("""
        SELECT
            u.id,
            u.name,
            u.email
        FROM Users u
        """)

        
        users = []

        
        dataset = db_cursor.fetchall()

        
        for row in dataset:

            user = Users(row['id'], row['name'], row['email'])

            users.append(user.__dict__)

    return users

def get_single_user(id):
    """docstring"""
    with sqlite3.connect("./journal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


        db_cursor.execute("""
        SELECT
            u.id,
            u.name,
            u.email
        
        FROM Users u
        WHERE u.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Users(data['id'], data['name'],data['email'])

    return entry.__dict__