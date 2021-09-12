from calendar import c
import sqlite3
from venv import create


def connectDB(db_path='database/users.db'):

    conn = None
    try:
        conn = sqlite3.connect(db_path)
        # print('Database succesffully opened!')

        conn.execute("""CREATE TABLE IF NOT EXISTS users(
                        NAME           TEXT    NOT NULL,
                        PASSWORD       TEXT     NOT NULL); """)

    except:
        print('Connection error!')
    return conn


def addUserDB(name, password):

    conn = connectDB()

    try:
        sql = ''' INSERT INTO users(NAME,PASSWORD)
                VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (name, password))
        conn.commit()
        print('User has been successfully created!')

    except:
        print('User could not created!')


def fetchUserDB(username):
    conn = connectDB()
    try:
        sql = ''' SELECT PASSWORD from users where name=? '''
        cur = conn.cursor()
        cur.execute(sql, (username, ))
        value = cur.fetchall()
        return value[0][0]

    except:
        print('User could not found!')
