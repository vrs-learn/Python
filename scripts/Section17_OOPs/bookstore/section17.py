#
# Writing code in OOP Style  i.e Object oriented design mode.
#
# Watch the frontend and backend python scripts in OOP style

class Database:

    def __init__(self): # __init__ is a initializer function of a class. i.e everytime a class is called, the __init__ function is called automatically.
        # it is necessary to keep self in the argument as its sent everytime the class is initialized.
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
        conn.commit()
        conn.close()
