import sqlite3 as sql3
import passlib.hash as phash
import sys

def insertUser(email,username,password):
    conn = sql3.connect("database.db")
    cur = conn.cursor()
    password = phash.bcrypt.hash(password)
    if not email or not username:
        sys.exit(1)
    cur.execute("INSERT OR IGNORE INTO users VALUES (?,?,?)",(email,username,password))
    conn.commit()
    conn.close()

def retrieveUser():
    conn = sql3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * From users")
    rows = cur.fetchall()
    l = []
    for i in rows:
        l.append(i)
    return l
