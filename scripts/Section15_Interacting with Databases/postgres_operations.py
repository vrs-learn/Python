
#
# Libraries for interacting with SQL Lite & PostGres
# sqllite -> sqlite3
# Postgres -> psycopg2
#
# Don't need to install sqllite3. it comes with python

import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password' host='192.168.0.106' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password' host='192.168.0.106' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" % (item,quantity,price)) # using string when running commands is a risky way of performing the activity.
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password' host='192.168.0.106' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password' host='192.168.0.106' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item = %s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password' host='192.168.0.106' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s where item = %s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
#insert("Grapes",10,15)
#insert("Coffee Cup",10,5)
#delete("Orange")
update(20,16.0,'Apple')
print(view())
