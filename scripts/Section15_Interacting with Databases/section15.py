#
# Libraries for interacting with SQL Lite & PostGres
# sqllite -> sqlite3
# Postgres -> psycopg2
#
# Don't need to install sqllite3. it comes with python

import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price)) # the ? is a best way of using the input variables.
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

create_table()
#insert("Coffee Cup",10,5)
print(view())
